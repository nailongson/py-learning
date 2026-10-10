def calculate_rectangle(width, height):
    area = width * height          # 面积
    perimeter = (width + height) * 2 # 周长
    return area, perimeter          # 同时返回两个值（本质上是一个 tuple）

# 用两个变量分别接住返回的多值
s, p = calculate_rectangle(5, 3)
print(f"面积: {s}, 周长: {p}")  # 输出: 面积: 15, 周长: 16