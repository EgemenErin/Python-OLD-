height = input("enter your height: ")
weight = input("enter your weight: ")
bmi = (float(weight) / (float(height)*float(height)))
print(str(weight) + " ÷ " + "(" + str(height) + " x " + str(height) + ")" + " = " + str(bmi))
if bmi  < 18.5:
    print(f"Your BMI is {bmi}, you are underweight.")
elif bmi > 18.5 and bmi < 25:
    print(f"Your BMI is {bmi}, you have a normal weight")
elif bmi > 25 and bmi < 30:
    print(f"Your BMI is {bmi}, you are slightly overweight.")
elif bmi > 30 and bmi < 35:
    print(f"Your BMI is {bmi}, you are obese.")
else:
    print(f"Your BMI is {bmi}, you are clinically obese.")