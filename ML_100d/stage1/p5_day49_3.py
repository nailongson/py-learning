import pandas as pd
orders = pd.DataFrame({"user": [1, 1, 2], "amount": [10, 20, 15]})
users = pd.DataFrame({"user": [1, 2], "region": ["east", "west"]})
joined = orders.merge(users, on="user", validate="many_to_one", indicator=True)
print(joined)
print(joined.groupby("region", dropna=False, observed=True)["amount"].sum())