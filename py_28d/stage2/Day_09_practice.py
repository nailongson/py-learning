# --- 任务 1：用 zip 把两个名单配对并遍历 ---
names = ["Alice", "Bob", "Charlie"]
scores = [85, 92, 78]

print("--- 任务 1:zip 配对遍历 ---")
# zip 会把两个列表对应的元素打包成一个个元组 (tuple)
for name, score in zip(names, scores):
  print(f"姓名: {name}, 分数: {score}")


# --- 任务 2：写 3 行代码踩一次 b = a 的坑 ---
print("\n--- 任务 2:b = a 的引用之坑 ---")
a = [1, 2, 3]  # 第 1 行：定义一个列表 a
b = a  # 第 2 行：把 a 赋值给 b（注意：这里传的是引用，不是复制！）
b.append(4)  # 第 3 行：修改 b，给它加个数字 4

print(f"修改 b 之后,a 的内容是: {a}")
print(f"修改 b 之后,b 的内容是: {b}")