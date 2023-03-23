height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
bmi = round(weight / (height ** 2))
if bmi <= 18.5:
    print(f"Your BMI is {bmi}, you are underweight.")
elif bmi <= 24.9:
    print(f"Your BMI is {bmi}, you have a normal weight.")
elif bmi <= 29.9:
    print(f"Your BMI is {bmi}, you are slightly overweight.")
elif bmi <= 34.9:
    print(f"Your BMI is {bmi}, you are obese.")
else: print(f"Your BMI is {bmi}, you are clinically obese.")
