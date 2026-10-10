# 1. 初始化通讯录（字典），包含部分初始数据（查的基础）
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