#Collect father input
#Collect son age 
#
#multiply son age by 2
#
#subtract it from father age
#
#wrap it in absolute function so that even if it is negative it will be turned to positive
#
#print the result



father_age = int(input ("Enter the father's age: "))

son_age = int(input ("Enter the son's age: "))

formular= father_age-(2*son_age)

abs_formular= abs(formular)

print(f"the result is {abs_formular}")


