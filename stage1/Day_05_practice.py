# 假设这是一组学生的成绩列表
scores = [85, 59, 92, 45, 78, 63, 90, 38]

# 1. 基本统计
total_score = sum(scores)          # 总分
count = len(scores)                # 人数
average_score = total_score / count if count > 0 else 0  # 平均分
max_score = max(scores)            # 最高分

# 2. 统计不及格个数 (< 60 分)
fail_count = 0
for score in scores:
    if score < 60:
        fail_count += 1

# 3. 打印结果
print(f"成绩列表: {scores}")
print(f"平均分: {average_score:.2f}")
print(f"最高分: {max_score}")
print(f"不及格个数: {fail_count}")

fruits = ["apple", "banana","apple"]
# 1. append: 末尾添加
fruits.append("orange")

# 2. insert: 指定索引插入（比如在索引 1 的位置插入 'grape'）
fruits.insert(1, "grape")# 输出: ['apple', 'grape','banana', "apple",'orange']

# 3.将索引 0 的元素修改为 "pear"
fruits[1] = "pear"# 输出: ['apple', 'pear', "apple",'orange']

# 4.查
# 1. 索引查询
print(fruits[1])          # 输出: pear

# 2. 存在性判断
print("apple" in fruits)  # 输出: True

# 3. 查找元素的索引位置
print(fruits.index("orange"))  # 输出: 4# 1. 初始化通讯录（字典），包含部分初始数据（查的基础）
contacts = {
    "张三": "13800138000",
    "李四": "13911112222"
}

print("--- 初始通讯录 ---")
for name, phone in contacts.items():
    print(f"姓名: {name}, 电话: {phone}")

# 2. 查 (Retrieve / Query)
# 使用 get() 安全取值，避免键不存在时报错
query_name = "张三"
print(f"\n[查] 查找 {query_name} 的电话：{contacts.get(query_name, '查无此人')}")

# 3. 增 (Create)
# 直接通过键赋值来添加新联系人
contacts["王五"] = "13722223333"
print("\n[增] 已添加 王五")

# 4. 改 (Update)
# 修改已有键对应的值
contacts["张三"] = "13888889999"
print("\n[改] 已修改 张三的电话")

# 5. 删 (Delete)
# 使用 del 删除指定键值对
del contacts["李四"]
print("\n[删] 已删除 李四")

# 6. 用 items() 打印全部 (Traverse & Print)
print("\n--- 最终通讯录 (items 遍历) ---")
for name, phone in contacts.items():
    print(f"姓名: {name} | 电话: {phone}")

# 4. 统计元素出现的次数
print(fruits.count("apple"))
print(fruits)  # 输出: ['apple', 'pear', 'banana',"apple",'orange']