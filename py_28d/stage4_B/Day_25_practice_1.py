import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import DataLoader
from torchvision import datasets, transforms

# 1. 准备 MNIST 数据集
transform = transforms.Compose([
    transforms.ToTensor(),
    transforms.Normalize((0.1307,), (0.3081,))
])

train_dataset = datasets.MNIST(root='./data', train=True, download=True, transform=transform)
train_loader = DataLoader(train_dataset, batch_size=64, shuffle=True)

# 2. 定义一个简单的神经网络模型
model = nn.Sequential(
    nn.Flatten(),
    nn.Linear(28 * 28, 128),
    nn.ReLU(),
    nn.Linear(128, 10)
)

# 3. 定义损失函数和优化器
criterion = nn.CrossEntropyLoss()
optimizer = optim.SGD(model.parameters(), lr=0.01)

# 4. 开始训练循环（以 1 个 Epoch 为例）
model.train()
running_loss = 0.0
correct = 0
total = 0

for epoch in range(18):  # 可以根据需要调整训练轮数
    for batch_idx, (data, target) in enumerate(train_loader):
        # 梯度清零
        optimizer.zero_grad()
        
        # ① model(x) 前向传播：计算预测输出
        outputs = model(data)
        
        # 计算 Loss
        loss = criterion(outputs, target)
        
        # ② loss.backward() 反向传播：计算梯度
        loss.backward()
        
        # ③ optimizer.step() 优化器更新参数
        optimizer.step()
        
        # 记录 Loss 和准确率
        running_loss += loss.item()
        _, predicted = outputs.max(1)
        total += target.size(0)
        correct += predicted.eq(target).sum().item()
        
        if batch_idx % 200 == 0:
            print(f'Epoch [{epoch}], Step [{batch_idx}/{len(train_loader)}], Loss: {loss.item():.4f}')

epoch_acc = 100. * correct / total
print((f'训练完成！准确率: {epoch_acc:.2f}%'))

# 保存模型权重
torch.save(model.state_dict(), 'mnist_model.pth')
print("模型已保存！")