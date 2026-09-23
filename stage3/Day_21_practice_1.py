import os
from dotenv import load_dotenv
from openai import OpenAI  # 或者使用 requests 库

# 加载 .env 文件
load_dotenv()

# 读取密钥
api_key = os.getenv("DEEPSEEK_API_KEY")

# 初始化客户端（以 OpenAI SDK 为例，DeepSeek 兼容 OpenAI 格式）
client = OpenAI(api_key=api_key, base_url="https://api.deepseek.com")

# 发送单次请求测试
response = client.chat.completions.create(
    model="deepseek-chat",
    messages=[
        {"role": "system", "content": "你是一个AI助手"},
        {"role": "user", "content": "你好，测试一下"}
    ],
    stream=False
)

print(response.choices[0].message.content)