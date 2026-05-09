#ask the user to enter the passoword
#
#use a couple of if statements to match the condition for the password strength
#

password= input("Enter the password:")

if len(password)>6 and  len(password) <= 10:

    print("medium")

elif len(password) < 6:

    print("weak")

elif len(password) >10:

    print("Strong")

elif len(password) < 1:

    print("invalid")


