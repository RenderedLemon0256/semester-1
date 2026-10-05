# Worksheet 1.2: Task 1 Solution
import sys
scoreInput = input("Enter your score")

try:
    score = int(scoreInput)
    if(score > 100 or score < 0 ):
        raise Exception("Error")
except:
    sys.exit("Error: Grade must be an integer between 0 and 100")

if(score >= 70):
    print(f"{score} is a Distinction")
elif(score >= 40):
    print(f"{score} is a Pass")
else:
    print(f"{score} is a Fail")