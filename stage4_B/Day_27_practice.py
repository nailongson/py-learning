from ultralytics import YOLO

# 加载官方最小号预训练模型（以 YOLOv8n 为例，也可以用yolo11n.pt）
model = YOLO("yolov8n.pt")

# 你的 3 张照片路径
image_paths = ["/Users/nailong/Documents/image1.jpg", "/Users/nailong/Documents/image2.jpg", "/Users/nailong/Documents/image3.jpg"]

# 运行推理并保存/展示结果
for path in image_paths:
    # predict 会自动检测物体、画出边界框、标出类别与置信度，并保存结果
    results = model(path, save=True, show=False)
    
    print(f"已完成 {path} 的检测，结果已保存。")