# 1. 接收用户输入并转换为浮点数（支持整数和小数）
num1 = float(input("请输入第一个数: "))
num2 = float(input("请输入第二个数: "))

# 2. 计算加减乘除
add_result = num1 + num2
sub_result = num1 - num2
mul_result = num1 * num2

# 注意：除法需要考虑除数是否为 0 的情况，这里先写基本逻辑
if num2 != 0:
    div_result = num1 / num2
else:
    div_result = "除数不能为零"

# 3. 使用 f-string 格式化输出结果
print(f"加法结果: {num1} + {num2} = {add_result}")
print(f"减法结果: {num1} - {num2} = {sub_result}")
print(f"乘法结果: {num1} * {num2} = {mul_result}")
print(f"除法结果: {num1} / {num2} = {div_result}")