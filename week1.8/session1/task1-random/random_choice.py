import random

# Read names from a file

with open("names.txt") as infile:
    names = [ line.strip() for line in infile ]

# Ask user to enter a number, then randomly choose that many names
numOfNames = int(input("How many names?: "))
# from the list, avoiding any duplicate choices
for i in range(0,numOfNames):
    index = random.randint(0,len(names)-1)
# Display the chosen names, one per line
    print(names[index])
    names.pop(index)
