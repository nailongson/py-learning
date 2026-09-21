def check_score(score):
    if score >= 60:
        return "及格"  # 满足这个条件，立刻把结果交出去并结束
    else:
        return "不及格" # 走另一条路交出结果
    
user_input = int(input("请输入一个成绩: "))
print(f"{check_score(user_input)}")
