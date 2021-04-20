import pandas as pd

df = pd.read_json("recipes.json")
df.to_csv("recipes.csv", index=False)