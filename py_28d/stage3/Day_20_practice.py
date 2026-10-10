import os
from dotenv import load_dotenv

# 加载 .env 文件
load_dotenv()

# 读取密钥
api_key = os.getenv("DEEPSEEK_API_KEY")

print("获取到的 Key 是:", api_key)
