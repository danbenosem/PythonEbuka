first_integer= int(input("Enter the first integer"))

second_integer= int(input("Enter the second integer"))


if second_integer!=0:
    result= first_integer/ second_integer
    print(result)

elif second_integer==0:
    print("Cannot be divided by zero")
