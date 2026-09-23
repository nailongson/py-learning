import torch
import torch.nn as nn

# 1. 定义一个两层全连接网络
class TwoLayerNet(nn.Module):
    def __init__(self, input_size, hidden_size, output_size):
        super(TwoLayerNet, self).__init__()
        # 第一层：线性变换 + ReLU 激活函数
        self.fc1 = nn.Linear(input_size, hidden_size)
        self.relu = nn.ReLU()
        # 第二层：线性变换
        self.fc2 = nn.Linear(hidden_size, output_size)

    def forward(self, x):
        out = self.fc1(x)
        out = self.relu(out)
        out = self.fc2(out)
        return out

# 2. 初始化网络（假设输入特征维度为 784，输出分类数为 10）
input_size = 784
hidden_size = 256  # 可在此处修改为 64 或 256
output_size = 10

model = TwoLayerNet(input_size, hidden_size, output_size)
print(f"当前隐藏层大小: {hidden_size}")

# 3. 观察和计算总参数量 (numel)
total_params = sum(p.numel() for p in model.parameters())
print(f"模型总参数量: {total_params}")

# 如果想看每层的参数量：
for name, param in model.named_parameters():
    print(f"{name}: {param.numel()} 个参数")