"""
自动记录电脑上正在使用的软件（macOS）

用法：
    python3 stage2/activity_tracker.py
然后用浏览器打开 http://127.0.0.1:8765

原理：
    - 每 5 秒问一次系统“现在最前面的是哪个软件”（lsappinfo 命令）
    - 同一个软件连续使用就延长它的结束时间，换软件就开一条新记录
    - 键盘鼠标 5 分钟没动算“离开”，这段时间不记
    - 记录按天存成 JSON：stage2/activity_log/2026-09-28.json
    - 同时开一个只有本机能访问的小网页服务器，给 todo.html 提供数据

只用到 Python 标准库，不需要 pip install。按 Ctrl+C 停止。
"""

import json
import re
import subprocess
import threading
import time
from datetime import date
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import parse_qs, urlsplit

HOST = "127.0.0.1"          # 只监听本机，局域网里的其他电脑访问不到
PORT = 8765
POLL_SECONDS = 5            # 多久检查一次
IDLE_SECONDS = 5 * 60       # 多久没操作算离开
MERGE_GAP = POLL_SECONDS * 3  # 同一个软件中断不超过这个时间，算同一段

BASE_DIR = Path(__file__).resolve().parent
HTML_FILE = BASE_DIR / "todo.html"
LOG_DIR = BASE_DIR / "activity_log"

lock = threading.Lock()     # 后台记录线程和网页请求会同时读写 records，用锁保护
state = {"day": None, "records": [], "idle": False, "last_seen": 0.0}


# ---------- 读取系统信息 ----------

def front_app():
    """返回最前面的软件名，拿不到时返回 None"""
    try:
        asn = subprocess.run(["lsappinfo", "front"], capture_output=True, text=True, timeout=3).stdout.strip()
        if not asn:
            return None
        out = subprocess.run(["lsappinfo", "info", "-only", "name", asn],
                             capture_output=True, text=True, timeout=3).stdout
        # 输出长这样："LSDisplayName"="终端"
        match = re.search(r'"LSDisplayName"="(.*)"', out)
        return match.group(1) if match else None
    except (OSError, subprocess.SubprocessError):
        return None


def idle_seconds():
    """键盘鼠标多久没动了（秒）"""
    try:
        out = subprocess.run(["ioreg", "-c", "IOHIDSystem", "-d", "4"],
                             capture_output=True, text=True, timeout=3).stdout
        match = re.search(r'"HIDIdleTime" = (\d+)', out)
        return int(match.group(1)) / 1_000_000_000 if match else 0   # 单位是纳秒
    except (OSError, subprocess.SubprocessError):
        return 0


# ---------- 按天读写记录 ----------

def log_file(day):
    return LOG_DIR / f"{day}.json"


def load_day(day):
    try:
        return json.loads(log_file(day).read_text(encoding="utf-8"))
    except (FileNotFoundError, json.JSONDecodeError):
        return []


def save_day(day, records):
    LOG_DIR.mkdir(exist_ok=True)
    tmp = log_file(day).with_suffix(".tmp")
    tmp.write_text(json.dumps(records, ensure_ascii=False, indent=1), encoding="utf-8")
    tmp.replace(log_file(day))   # 先写临时文件再替换，程序中途被关掉也不会写坏


# ---------- 后台记录 ----------

def record_once():
    now = time.time()
    today = date.today().isoformat()
    app = front_app()
    idle = idle_seconds() >= IDLE_SECONDS

    with lock:
        if state["day"] != today:           # 过了零点，换一个新文件
            state["day"] = today
            state["records"] = load_day(today)

        state["idle"] = idle
        if idle or not app:
            return

        records = state["records"]
        last = records[-1] if records else None
        if last and last["app"] == app and now - last["end"] <= MERGE_GAP:
            last["end"] = now
        else:
            records.append({"app": app, "start": now, "end": now})
        state["last_seen"] = now
        save_day(today, records)


def tracker_loop():
    while True:
        record_once()
        time.sleep(POLL_SECONDS)


def snapshot(day=None):
    """给网页用的数据：今天的最后一条如果还在进行，标上 current；传了 day 就读那天的文件"""
    with lock:
        if day and day != state["day"]:
            return {"day": day, "idle": False, "records": load_day(day)}
        records = [dict(r) for r in state["records"]]
        idle = state["idle"]
        if records and not idle and time.time() - records[-1]["end"] <= MERGE_GAP:
            records[-1]["current"] = True
    return {"day": state["day"], "idle": idle, "records": records}


def parse_day(value):
    """只接受 YYYY-MM-DD 格式的真实日期，防止用 ../ 之类读到别的文件"""
    try:
        return date.fromisoformat(value).isoformat() if re.fullmatch(r"\d{4}-\d{2}-\d{2}", value) else None
    except ValueError:
        return None


# ---------- 网页服务器 ----------

class Handler(BaseHTTPRequestHandler):
    def send_json(self, data, status=200):
        body = json.dumps(data, ensure_ascii=False).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Cache-Control", "no-store")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def do_GET(self):
        path = self.path.split("?")[0]
        if path in ("/", "/todo.html"):
            # 只提供这一个页面，不把整个文件夹暴露出去
            body = HTML_FILE.read_bytes()
            self.send_response(200)
            self.send_header("Content-Type", "text/html; charset=utf-8")
            self.send_header("Content-Length", str(len(body)))
            self.end_headers()
            self.wfile.write(body)
        elif path == "/api/activity":
            query = parse_qs(urlsplit(self.path).query)
            if "date" in query:
                day = parse_day(query["date"][0])
                if day is None:
                    return self.send_json({"error": "bad date"}, 400)
                self.send_json(snapshot(day))
            else:
                self.send_json(snapshot())
        else:
            self.send_json({"error": "not found"}, 404)

    def do_POST(self):
        # 只接受本页面发来的请求，防止别的网站偷偷让浏览器调用清空接口
        origin = self.headers.get("Origin")
        if origin and origin not in (f"http://{HOST}:{PORT}", f"http://localhost:{PORT}"):
            return self.send_json({"error": "forbidden"}, 403)

        if self.path == "/api/activity/clear":
            with lock:
                state["records"] = []
                if state["day"]:
                    save_day(state["day"], [])
            self.send_json({"ok": True})
        else:
            self.send_json({"error": "not found"}, 404)

    def log_message(self, *args):
        pass   # 不在终端刷屏打印每个请求


def main():
    if front_app() is None:
        print("读取不到当前软件，这个脚本只支持 macOS。")
        return

    threading.Thread(target=tracker_loop, daemon=True).start()
    server = ThreadingHTTPServer((HOST, PORT), Handler)
    print(f"开始记录，每 {POLL_SECONDS} 秒检查一次，记录保存在 {LOG_DIR}")
    print(f"用浏览器打开 http://{HOST}:{PORT}   （按 Ctrl+C 停止）")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\n已停止记录。")
    finally:
        server.server_close()


if __name__ == "__main__":
    main()
