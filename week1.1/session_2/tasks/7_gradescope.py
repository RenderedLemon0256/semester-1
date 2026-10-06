# To test that you can successfully download a file and upload it to gradescope

# You are going to write a very simple program:

# Ask a user to enter two numbers (one per input)
num1Input = input("Enter first number ")
num2Input = input("Enter second number ")

num1 = 0.0
num2 = 0.0
try:
    num1 = float(num1Input)
    num2 = float(num2Input)
except:
    print("That is not a number")
    exit()

print(num1 * num2)
# multiply those numbers together

# print out the result

# There is an extra point available for validating that they entered numbers!
# Add to your code so that if they entered something other than an integer it prints
# 'That is not a number' and exits.

# Download your file, and upload it to the 'Week 1 Session 2 - Practice Upload' task on Minerva.
# You will get some feedback - ensure you are passing the tests!