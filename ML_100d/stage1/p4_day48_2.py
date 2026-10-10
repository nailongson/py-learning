import pandas as pd
a = pd.DataFrame({"name": ["A", "B"], "score": pd.Series([80, None], dtype="Int64")})
b = pd.DataFrame({"name": ["C"], "score": [90]})
combined = pd.concat([a, b], ignore_index=True)
combined.loc[combined["score"].isna(), "score"] = 0
print(combined)