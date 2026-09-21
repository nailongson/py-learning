# 模拟输入的标准日志行
log_line = "2026-06-06 10:00:00 [INFO] 系统启动成功"

# 方法一：使用 split() 按空格切分
# maxsplit=3 表示最多切成 4 部分，保留后面的整体内容
parts = log_line.split(" ", 3)

if len(parts) >= 4:
    date_part = parts[0] + " " + parts[1]  # 日期 + 时间
    level_part = parts[2]                    # 级别
    content_part = parts[3]                  # 内容
    
    print(f"日期: {date_part}")
    print(f"级别: {level_part}")
    print(f"内容: {content_part}")
else:
    print("日志格式不匹配")