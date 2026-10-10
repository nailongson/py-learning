import pandas as pd
df = pd.DataFrame({"time": pd.date_range("2024-01-01", periods=5, tz="UTC"), "sales": [3, 5, 4, 8, 9]})
df = df.set_index("time")
df["past_mean"] = df["sales"].shift(1).rolling(2).mean()
print(df)
print(df["sales"].resample("2D").sum())