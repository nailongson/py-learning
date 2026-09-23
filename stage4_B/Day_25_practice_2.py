import torch
import torch.nn as nn
from torchvision import transforms
from PIL import Image, ImageOps

# 1. 重新定义和训练时一模一样的模型结构
model = nn.Sequential(
    nn.Flatten(),
    nn.Linear(28 * 28, 128),
    nn.ReLU(),
    nn.Linear(128, 10)
)

# 2. 加载刚才保存的权重
model.load_state_dict(torch.load('mnist_model.pth'))
model.eval()  # 切换到评估模式

# 3. 定义和训练时完全一致的图像预处理流程
transform = transforms.Compose([
    transforms.Resize((28, 28)),          # 缩放到 28x28 像素
    transforms.Grayscale(num_output_channels=1), # 转为单通道灰度图
    transforms.ToTensor(),                # 转为 Tensor 并且像素值归一化到 [0, 1]
    transforms.Normalize((0.1307,), (0.3081,)) # 使用和 MNIST 一样的均值和标准差
])

def predict_my_image(image_path):
    # 打开你的手写图片
    image = Image.open(image_path)
    
    # ⚠️ 关键点：MNIST 是“黑底白字”，如果你在白纸上用黑笔写，需要反转颜色！
    # 如果你已经是黑底白字，可以把下面这行注释掉
    image = ImageOps.invert(image)
    
    # 预处理
    image_tensor = transform(image).unsqueeze(0) # 增加一个 Batch 维度 [1, 1, 28, 28]
    
    # 预测
    with torch.no_grad():
        outputs = model(image_tensor)
        _, predicted = torch.max(outputs, 1)
        
    print(f"🎉 模型预测结果是: {predicted.item()}")

# 4. 测试你拍的照片或画的图片
predict_my_image(image_path="/Users/nailong/Documents/py learning/text_image.jpg") # 把这里换成你的图片路径