#generate two random numbers
#use those numbers to be generating subtraction problems that are not negative
#the user can only take 10 questions so set up loop for that
#if the user fails once give him another attempt , he can only attempt twice 
#display final score based on the correct score, will use count for that
#















import random
score=0

def generate_subtraction_problem():
    number1=random.randint(1,12)
    number2= random.randint(1,12)

    
    newnum= max(number1,number2)
    newnum2= min (number1,number2)

    correct_answer= newnum-newnum2

    return newnum,newnum2,correct_answer

def ask_question():
    
    global score
    
    newnum,newnum2,correct_answer  =  generate_subtraction_problem()
    print(f"what is {newnum}-{newnum2}")
    answer= int(input("your answer: "))
    if answer==correct_answer:
        print("correct")
        score+=1
    else: 
        print(f"what is {newnum}-{newnum2}")
        answer= int(input("your answer: "))
        if answer==correct_answer:
            print("correct")
            score+=1
        else:
            print(f"answer is {correct_answer}")


def final_score():
    print(f"you got {score} out of 10")




  


























