#5个学生信息
message = [
    {"name":"张三","score":"98"},
    {"name":"李四","score":"59"},
    {"name":"王五","score":"88"},
    {"name":"赵六","score":"78"}
]

#增加一个人
new_person={"name":"苏七","score":"35"}
message.append(new_person)
print(f"已增加一人:{new_person['name']}")

#查找李四
print("-----查找李四-----")
aim_person="李四"
for person in message:
    if person["name"] == "李四":
        print(f"姓名:{aim_person}\n分数:{person['score']}")

#改变李四信息
print("-----改变李四信息-----")
for i in message:
    if i["name"] == "李四":
        i["score"] = "50"
        print(f"姓名:{aim_person}\n分数:{i['score']}") 

#删掉李四
print("-----删掉李四-----")
for i in message:
    if i['name'] == "李四":
        message.remove(i)
        print(f"已经删掉{i['name']}")

#插入王小明
new_guy={"name":"王小明","score":"44"}
message.insert(1,new_guy)
print(f"成功插入{new_guy['name']}")

#平均分
total_score = sum(int(person['score']) for person in message)
total_person = len(message)
average_score = total_score /total_person 
print(f"平均分:{average_score}")

#不及格人数
i=0
for person in message:
    if int(person['score']) < 60:
        i+=1
print(f"不及格人数:{i}")

#不及格名单
print("不及格名单:")
for person in message:
    if int(person['score']) < 60:
       print(f"{person['name']}")