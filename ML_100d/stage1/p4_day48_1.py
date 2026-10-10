import pandas as pd

# 准备带标签的数据
df = pd.DataFrame(
    {"score": [95.5, 82.0, 89.5], "grade": ["A", "B", "B+"]},
    index=["Alice", "Bob", "Charlie"],
)
# 1. 取单格标量值
print(df.loc["Alice", "score"])  # 95.5

# 2. 取某一行（返回 Series）
print(df.loc["Bob"])

# 3. 按标签切片（注意：.loc 切片是“包含两端”的闭区间！）
print(df.loc["Alice":"Bob", "score":"grade"])

# 筛选 score >= 85 的行，并且只取 grade 列
top_grades = df.loc[df["score"] >= 85, "grade"]

# 修改特定标签位置的值
df.loc["Bob", "score"] = 85.0

# 条件赋新值（避免 SettingWithCopyWarning 的规范写法）
df.loc[df["score"] >= 90, "grade"] = "A+"

# 插入整列新标签
df.loc[:, "passed"] = True

#追加单行数据
df.loc["Eva"] = [78.0, "C", True]

print(df)