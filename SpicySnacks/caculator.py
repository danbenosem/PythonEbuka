# ask for the first number
#
#ask for the sccond number
#
#ask for the operator
#
#then use if statements to match them
#
#perform the calculation


first_number= int(input("Enter the first number:"))

second_number= int(input("Enter the second number:"))


print("Enter the operator you want, by entering the number beside it")
print("\n")
print("1. +  ")
print("2. -  ")
print("3. *  ")
print("4. /  ")
print("\n")


user_operator= input("Enter operator:")


if user_operator== "1":
    print("The answer is ",(first_number+second_number))

elif user_operator== "2":
    print("The answer is ",(first_number-second_number))

elif user_operator== "3":
    print("The answer is ",(first_number*second_number))

elif user_operator== "4":
    print("The answer is ",(first_number/second_number))

















