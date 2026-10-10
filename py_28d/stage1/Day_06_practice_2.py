# 用列表嵌套字典，模拟多个人的“messages”结构
contacts_list = [
    {"role": "user", "name": "张三", "phone": "13800138000", "status": "在线"},
    {"role": "user", "name": "李四", "phone": "13911112222", "status": "忙碌"},
    {"role": "user", "name": "王五", "phone": "13722223333", "status": "离线"}
]

print("--- 多人群组通讯录 ---")
# 遍历每个人员的信息
for person in contacts_list:
    print(f"姓名: {person['name']} | 电话: {person['phone']} | 状态: {person['status']}")

# 增：再拉一个人进群
new_person = {"role": "user", "name": "赵六", "phone": "13666668888", "status": "在线"}
contacts_list.append(new_person)
print(f"\n[增] 新成员 {new_person['name']} 已加入群聊！")

# 查：查找某个人的状态
target_name = "李四"
print(f"\n[查] 查找成员：")
for person in contacts_list:
    if person["name"] == target_name:
        print(f"找到了！{target_name} 的电话是 {person['phone']}，当前状态：{person['status']}")

# 改：修改赵六的状态
for person in contacts_list:
    if person["name"] == "赵六":
        person["status"] = "正在疯狂打代码"
        print(f"\n[改] 已更新 {person['name']} 的状态为：{person['status']}")

# 删：把王五移除群聊
for person in contacts_list:
    if person["name"] == "王五":
        contacts_list.remove(person)
        print(f"\n[删] 已将 {person['name']} 移出群聊")

# 最终用 items/遍历打印完整名单
print("\n--- 最终群成员名单 ---")
for person in contacts_list:
    # 利用 .items() 遍历字典内部的键值对
    print(f"--- 成员详情 ---")
    for key, value in person.items():
        print(f"{key}: {value}")
        