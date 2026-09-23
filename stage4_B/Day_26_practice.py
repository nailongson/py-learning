import matplotlib.pyplot as plt
import torch
import torch.nn as nn
from torch.utils.data import DataLoader
from torchvision import datasets, transforms

# 1. 准备测试集数据
transform = transforms.Compose(
    [transforms.ToTensor(), transforms.Normalize((0.1307,), (0.3081,))]
)

test_dataset = datasets.MNIST(
    root="./data", train=False, download=True, transform=transform
)
test_loader = DataLoader(test_dataset, batch_size=1000, shuffle=False)

# 2. 定义模型结构（需与训练时保持完全一致）
model = nn.Sequential(
    nn.Flatten(), nn.Linear(28 * 28, 128), nn.ReLU(), nn.Linear(128, 10)
)

# 3. 练习要求：加载模型权重
# 假设你在之前训练完后用 torch.save(model.state_dict(), 'mnist_model.pth') 保存了权重
model.load_state_dict(torch.load("mnist_model.pth"))
model.eval()  # 切换到评估模式

# 4. 练习要求：报测试集准确率 & 收集错分样本
correct = 0
total = 0
wrong_samples = []  # 用于存放错分样本 (图片, 预测值, 真实值)

with torch.no_grad():
  for data, target in test_loader:
    outputs = model(data)
    _, predicted = torch.max(outputs, 1)

    total += target.size(0)
    correct += (predicted == target).sum().item()

    # 找出当前 batch 中预测错的样本
    matches = predicted == target
    for i in range(len(matches)):
      if not matches[i] and len(wrong_samples) < 6:
        wrong_samples.append((data[i], predicted[i].item(), target[i].item()))

test_acc = 100. * correct / total
print(f"🎯 测试集准确率: {test_acc:.2f}%")

# 5. 练习要求：画 6 个错分样本并分析
fig, axes = plt.subplots(2, 3, figsize=(9, 6))
axes = axes.ravel()

for idx, (img, pred, true) in enumerate(wrong_samples):
  # 将 Tensor 转回可显示的图片格式 (28x28)
  img = img.squeeze(0) * 0.3081 + 0.1307  # 反归一化（可选，方便看）

  axes[idx].imshow(img, cmap="gray")
  axes[idx].set_title(f"Pred: {pred} | True: {true}", color="red")
  axes[idx].axis("off")

plt.suptitle("MNIST Misclassified Samples Analysis", fontsize=14)
plt.tight_layout()
plt.show()