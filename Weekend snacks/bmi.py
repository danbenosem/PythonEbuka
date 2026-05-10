weight= int(input("Enter the weight"))

height= int(input("Enter the height"))

bmi=weight/(height*height)

if bmi < 18.5:
    print("Underweight")

if bmi >= 18.5 and bmi<= 24.9 :
    print("Normal")

if bmi>= 25 and  bmi <=29.9:
 print("Overweight")


if bmi >=30:
    print("Obese")
