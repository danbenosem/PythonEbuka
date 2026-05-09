#enter the user the user input
#
#use an if statement that matches the conditions
#which are as follows
#
#Codethat Checks if a year is a
#Leap Year. A year is leap if:
#● Divisible by 4
#● BUT not by 100
#● UNLESS also by 400



year= int(input("Enter the year:"))


if (year % 4=0  and year % 100 !=0) or (year % 400= 0):
    print(f"{year} is a leap year")


