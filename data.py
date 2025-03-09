import json
import pandas as pd
#import random

with open("allergy_recipes.json", "r", encoding="utf-8") as f1, open("diabetes_search.json", "r", encoding="utf-8") as f2,  open("diet_recipes.json", "r", encoding="utf-8") as f3:
    data1 = json.load(f1)
    data2 = json.load(f2)
    data3 = json.load(f3)

merged_data = {"recipes": data1["recipes"] + data2["recipes"] + data3["recipes"]}

df = pd.DataFrame(merged_data["recipes"])

for column in ["diabetes", "category", "diet", "allergy", "type"]:
    df[column] = df[column].apply(lambda x: x[0] if isinstance(x, list) and len(x) == 1  else x)
#df["price"] = df["price"].apply(lambda x: random.randint(90, 300))

for column in ["class", "type"]:
    if column in df.columns:
        df[column] = df[column].apply(lambda x: [item.lower() for item in x] if isinstance(x, list) else (x.lower() if isinstance(x, str) else x))

df.to_csv("recipes_data.csv", index=False, encoding="utf-8-sig")