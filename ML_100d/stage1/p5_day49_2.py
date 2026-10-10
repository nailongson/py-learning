import pandas as pd

df = pd.DataFrame({
    "name": ["Alice", "Alice", "Bob"],
    "day": ["Mon", "Mon", "Tue"],
    "hours": [3, 5, 8]
})
# 试图将 day 展开为列
# df.pivot(index="name", columns="day", values="hours")

# 指定用求和聚合. aggfunc默认是mean  fill_value默认是NaN
# 透视表本质上是把两组离散维度拉成一个矩阵网格
res = df.pivot_table(index="name", columns="day", values="hours", aggfunc="sum", fill_value=0)
print(res)