import random

# 1. 生成一个 1 到 100 之间的随机数
target_number = random.randint(1, 100)
count = 0  # 记录猜测次数

print("--- 欢迎来到猜数字游戏！---")
print("我已经想好了一个 1 到 100 之间的数字，你来猜猜看。")

# 2. 使用 while 循环让用户不断猜测，直到猜中为止
while True:
    try:
        guess = int(input("请输入你猜的数字: "))
    except ValueError:
        print("无效输入，请输入一个整数！")
        continue

    count += 1  # 每次输入有效数字，次数加 1

    # 3. 条件判断
    if guess < target_number:
        print("太小了，再往大猜一点！")
    elif guess > target_number:
        print("太大了，再往小猜一点！")
    else:
        print(f"恭喜你！猜对了！神秘数字就是 {target_number}。")
        print(f"你总共猜了 {count} 次。")
        break  # 猜中后跳出循环