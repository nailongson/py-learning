import pandas as pd
#merge学习
# 员工基本信息（左表）df_staff
df_staff = pd.DataFrame({
    "emp_id": [101, 102, 103, 104],
    "dept_id": ["D1", "D2", "D1", "D3"],
    "name": ["Alice", "Bob", "Charlie", "David"]
})

# 部门信息（右表）df_dept
df_dept = pd.DataFrame({
    "department_code": ["D1", "D2", "D4"],
    "dept_name": ["HR", "Engineering", "Marketing"]
})

#1
# res = pd.merge(
#     df_staff, 
#     df_dept, 
#     left_on="dept_id", 
#     right_on="department_code", 
#     how="inner"
# )

#2
# 左右表同时匹配多个键
# res = pd.merge(
#     df1,
#     df2,
#     on=["store_id", "product_id"], 
#     how="left")
#how="left" 
# 表示左连接（Left Join），
# 它的核心规则是：以左表为主体，左表的所有行必须全部保留；
# 右表只负责提供能匹配上的补充信息，
# 匹配不上的位置填缺失值（NaN / <NA>）。
# 确保右表对于同一个 dept_id 是唯一的，防止笛卡尔积扩散
res = pd.merge(
    df_staff, 
    df_dept, 
    left_on="dept_id", 
    right_on="department_code", 
    how="left",
    validate="many_to_one" , # 若右表出现重复部门代码，直接抛出 MergeError
    indicator=True  # 开启状态标记
)

#剔除冗余连接键列
res = res.drop(columns=["department_code"])
#填充未匹配值
#用fillna赋予默认值
res["dept_name"] = res["dept_name"].fillna("Unknown")
print(res)

print(res[["emp_id", "name", "dept_id", "_merge"]])