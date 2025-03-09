import json
import random


with open("allergy_recipes.json", "r", encoding="utf-8") as f1, open("diabetes_search.json", "r", encoding="utf-8") as f2,  open("diet_recipes.json", "r", encoding="utf-8") as f3:
    data1 = json.load(f1)
    data2 = json.load(f2)
    data3 = json.load(f3)


for recipe in data1["recipes"]:
        recipe["price"] = random.randint(90, 300)
with open("allergy_recipes.json", "w", encoding="utf-8") as f1:
    json.dump(data1, f1, ensure_ascii=False, indent=4)
    
    
for recipe in data2["recipes"]:
        recipe["price"] = random.randint(90, 300)
with open("diabetes_search.json", "w", encoding="utf-8") as f2:
    json.dump(data2, f2, ensure_ascii=False, indent=4)
    
    
for recipe in data3["recipes"]:
        recipe["price"] = random.randint(90, 300)
with open("diet_recipes.json", "w", encoding="utf-8") as f3:
    json.dump(data3, f3, ensure_ascii=False, indent=4)