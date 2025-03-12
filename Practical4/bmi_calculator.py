# 1. Define variables for weight (in kg) and height (in meters)
# 2. Calculate BMI using the formula: BMI = weight / (height ** 2).
# 3. Determine the weight category based on BMI.
# 4. Print the BMI and weight category.
weight = float(input("weight:"))  # Input weight
height = float(input("height"))  # Input height

# Calculate BMI
bmi = weight / (height ** 2)

# Determine weight category
if bmi < 18.5:
    category = "underweight"
elif 18.5 <= bmi < 30:
    category = "normal weight"
else:
    category = "obese"

print("Your BMI is",bmi, "You are considered",category)
# Print the result