first_integer= int(input("Enter the first number"))

second_integer= int(input("Enter the second number"))


third_integer= int(input("Enter the third number"))


largest= first_integer


if second_integer > largest:
    largest= second_integer


if third_integer > largest:

    largest=third_integer


print(largest)
