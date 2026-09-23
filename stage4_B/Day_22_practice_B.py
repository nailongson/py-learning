import torch

# 打印 PyTorch 版本和 CUDA 可用性
print("PyTorch 版本:", torch.__version__)
print("CUDA 是否可用:", torch.cuda.is_available())

# 创建一个 2x3 的二维张量
x = torch.tensor([[1.0, 2.0, 3.0], 
                  [4.0, 5.0, 6.0]])
print("创建的张量 x:\n", x)
print("张量的形状 (shape):", x.shape)

# 对应元素相加
y = x + 10
print("x + 10 的结果:\n", y)

# 对应元素相乘
z = x * 2
print("x * 2 的结果:\n", z)

# 把原本 2x3 的张量 reshape 成 3x2 的张量
x_reshaped = x.reshape(3, 2)
print("变形成 3x2 后的张量:\n", x_reshaped)