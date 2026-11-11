height = float(input("Enter your height in meters: "))
weight = float(input("Enter your weight in kilograms: "))       
bmi = weight/(height ** 2)
if bmi >= 30:
    print("obesity")
elif bmi >= 25 and bmi < 30:
    print("overweight")
elif bmi >= 18.5 and bmi <= 25:
    print("normal")
else:
    print("underweight")