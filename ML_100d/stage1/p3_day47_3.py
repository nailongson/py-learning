import numpy as np

# 1. 定义字段与对应的数据类型
# 'U10': 最多 10 个字符的 Unicode 字符串；'f4': 32 位浮点数 (float32)
dt = np.dtype([('name', 'U10'), ('score', np.float32)])

# 2. 准备数据（元组列表格式）
data = [
    ('Alice', 95.5),
    ('Bob', 82.0),
    ('Charlie', 89.5)
]

# 3. 创建结构化数组
arr = np.array(data, dtype=dt)

print("结构化数组：\n", arr)
print("数组 dtype：\n", arr.dtype)