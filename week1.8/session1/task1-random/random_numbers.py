import random

# Get user to input how many random numbers they want
numOfNums = int(input("How many numbers?: "))
# Generate this many random numbers

# Write the random numbers to a file named random.txt, one number per line
with open("week1.8/session1/task1-random/random.txt","w") as f:
    for i in range(0,numOfNums):
        f.write(str(random.randint(0,100000)) + '\n')
