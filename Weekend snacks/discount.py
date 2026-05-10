total_bill= int(input("what is the total bill"))

is_member=input("are you a member? yes or no")


if total_bill >= 1000 and is_member=="yes":
    print(total_bill-(total_bill*0.1))

if total_bill >= 1000 and is_member=="no":
    print(total_bill-(total_bill*0.5))

else: 
    print("no discount")



