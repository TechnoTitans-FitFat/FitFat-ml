import pandas as pd
import random
from faker import Faker

fake = Faker()

genders = ["Male", "Female"]
allergies = ["Peanuts", "Wheat", "Shellfish", "Lactose", "None"]
diabetes_types = ["Type 1", "Type 2", "None"]
#blood_sugar_ranges = ["70-120", "80-130", "85-135", "90-140"]
diets = ["Keto","Vegan","Low-Carb","High-Carb","None"]

min_sugar = random.randint(70, 90)
max_sugar = random.randint(min_sugar + 10, 180)

data = []
for _ in range(1000):  
    gender = random.choice(genders)
    dob = fake.date_of_birth(minimum_age=18, maximum_age=90)
    height = random.randint(150, 200)
    weight = random.randint(45, 120)
    allergy = random.choice(allergies)
    diet = random.choice(diets)
    diabetes = random.choice(diabetes_types)
    insulin_coefficient = f"{1}-{random.randint(5, 20)}" if diabetes == "Type 1" else None
    blood_sugar_range = f"{min_sugar}-{max_sugar}" if diabetes != "None" else None
    
    data.append([
        gender, dob, height, weight, allergy, diet, diabetes, insulin_coefficient, blood_sugar_range
    ])

df = pd.DataFrame(data, columns=[
    "Gender", "Date of Birth", "Height (cm)", "Weight (kg)", "Allergy", "Diet",
    "Diabetes", "Insulin Coefficient", "Preferred Blood Sugar Range"
])

df.to_csv("synthetic_health_data.csv", index=False)
