passed = 0
failed = 0
pass_mark = 45

print("Enter the scores for 15 students:")

for i in range(15):
   
    score = int(input("Enter score: "))
    
    if score >= pass_mark:
        passed = passed + 1
    else:
        failed = failed + 1

print("Number of students that passed:", passed)
print("Number of students that failed:", failed)
