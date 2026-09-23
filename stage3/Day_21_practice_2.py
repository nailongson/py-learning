import os
from dotenv import load_dotenv
import requests
import json

# 1. 加载 .env 文件并读取密钥
load_dotenv()
api_key = os.getenv("DEEPSEEK_API_KEY")

if not api_key:
    raise ValueError("未找到 DEEPSEEK_API_KEY，请检查 .env 文件！")

# 2. 定义 API 的请求地址和请求头
url = "https://api.deepseek.com/chat/completions"
headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {api_key}"
}

# # 3. 初始化 messages 列表（这是实现多轮对话的“记忆日记本”）
# messages = [
#     {"role": "system", "content": "你是一个乐于助人的命令行 AI 助手。"}
# ]
HISTORY_FILE = "chat_history.json"

# 检查本地有没有历史聊天记录文件
if os.path.exists(HISTORY_FILE):
    with open(HISTORY_FILE, "r", encoding="utf-8") as f:
        messages = json.load(f)
        print("=== 已成功加载上一次的聊天记录！===")
else:
    # 如果没有，就用初始的人设
    messages = [
        {"role": "system", "content": "你是一个乐于助人的命令行 AI 助手。"}
    ]

print("=== DeepSeek CLI 聊天机器人已启动 (输入 'quit' 或 'exit' 退出) ===")

while True:
    # 获取用户输入
    user_input = input("\n你：").strip()
    
    # 检查是否退出
    if user_input.lower() in ["quit", "exit"]:
        print("再见！")
        break
    
    if not user_input:
        continue

    # 将用户的输入追加到 messages 列表中
    messages.append({"role": "user", "content": user_input})

    # 组装发给 API 的完整数据（每次把累积的所有历史对话全量发过去）
    payload = {
        "model": "deepseek-chat",
        "messages": messages,
        "stream": False
    }

    try:
        # 发送 POST 请求
        response = requests.post(url, json=payload, headers=headers)
        response.raise_for_status() # 检查请求是否成功
        
        # 解析返回的 JSON 数据
        result = response.json()
        assistant_reply = result["choices"][0]["message"]["content"]
        
        print(f"AI：{assistant_reply}")

        # 将大模型的回复也追加到 messages 列表中，以便下一轮带上
        messages.append({"role": "assistant", "content": assistant_reply})

        # 把当前的 messages 整个保存到本地 json 文件中
        with open(HISTORY_FILE, "w", encoding="utf-8") as f:
            json.dump(messages, f, ensure_ascii=False, indent=2)
            
    except requests.exceptions.RequestException as e:
        print(f"请求发生错误：{e}")