# 假设这是全班应到名单（或签到名单1）与实际到场名单（或签到名单2）
registered_list = ["张三", "李四", "王五", "赵六", "孙七"]
signed_in_list = ["张三", "王五", "赵六", "孙七", "周八"] # 周八可能是代签或新来的人

# 1. 数据去重与转换成集合
all_registered = set(registered_list)
actual_signed = set(signed_in_list)

# 2. 找缺勤（应到名单中存在，但实到名单中没有的）
absent_people = all_registered - actual_signed
print(f"缺勤人员: {absent_people}")

# 3. 统计实到率
# 实到人数（以应到为基准的实际出勤人数，即交集）
attended_on_time = all_registered & actual_signed
attendance_rate = len(attended_on_time) / len(all_registered) * 100
print(f"实到率: {attendance_rate:.2f}%")

# 4. 额外：总共出现过的人（并集）与重复去重
total_unique_people = all_registered | actual_signed
print(f"汇总去重总人数: {total_unique_people}")