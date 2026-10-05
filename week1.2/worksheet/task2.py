# Worksheet 1.2: Task 2 Solution
from util import read_numbers
import sys

try:
    numbers = read_numbers()
    
    print(f"Minimum = {min(numbers)} ")
    print(f"Maximum = {max(numbers)} ")
    print(f"Mean = {sum(numbers) / len(numbers)} ")
except:
    sys.exit("Error: no numbers provided")

numbers.sort()
if(len(numbers) % 2 == 1): #odd number 
    print(f"Median = {numbers[(int(len(numbers) + 1) / 2)-1]} ")
else:
    firstMiddle = numbers[(len(numbers)/2)-1]
    secondMiddle = numbers[(len(numbers)/2)]
    sum = firstMiddle + secondMiddle
    print(f"Median = {sum / 2}" )

    