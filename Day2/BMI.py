weight = float(input("Enter your weight in kg: "))
height = float(input("Enter your height in meters: "))
bmi = round(weight / (height ** 2))
print(f"Your BMI is: {bmi}")