#set the count to run only three times for the loop
#that is to collect three averages
#
#calculate the average
#
#
#write if statements to satify the conditions listed in the question
#match the scores with the condition
#
#if the score fulfills any of the condition, print the output 





count=0;

total=0

while(count<3):

    score=int(input("Enter the score:"))
    
    total= total+score
    count+=1

average=total/3


if average>= 90 and average <= 100:
    print("A")

    count+=1

elif average>= 80 and average <90:
    print("B")
    count+=1

elif average>= 70 and average < 80:
    print("C")
    count+=1
    

elif average>= 60 and average < 70:
    print("D")
    count+=1

elif average> 90 and average < 60:
    print("F")
    count+=1

else:
    print("invalid")

    
    
