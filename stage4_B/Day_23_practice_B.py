import matplotlib.pyplot as plt
import torch
from torch.utils.data import DataLoader
from torchvision import datasets, transforms

# 1. 定义数据预处理（转换为 Tensor）
transform = transforms.Compose([transforms.ToTensor()])

# 2. 加载 MNIST 训练数据集
train_dataset = datasets.MNIST(
    root="./data", train=True, transform=transform, download=True
)

# 3. 使用 DataLoader 进行 batch 分批（这里设置 batch_size 能够满足获取 9 张以上即可）
train_loader = DataLoader(dataset=train_dataset, batch_size=9, shuffle=True)

# 4. 获取一个 batch 的数据和标签
images, labels = next(iter(train_loader))

print(f"数据 Tensor 形状: {images.shape}")  # 应该是 torch.Size([9, 1, 28, 28])
print(f"对应的标签: {labels}")

# 5. 使用 matplotlib 可视化 9 张手写数字
fig, axes = plt.subplots(3, 3, figsize=(6, 6))
for i, ax in enumerate(axes.flatten()):
    # 转换为 (28, 28) 的二维数组进行显示
    ax.imshow(images[i].squeeze(0), cmap="gray")
    ax.axis("off")
    ax.set_title(f"Label: {labels[i].item()}")

plt.tight_layout()
plt.show()