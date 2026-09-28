"""Advanced Task 5: Safe Divider
- Ask for a numerator and a denominator.
- Convert both inputs to integers and divide them to get a result.
- Use try/except to catch both non-numeric input and division by zero, giving useful messages for each case.
- Only print the final answer when the calculation succeeds.
"""

numerator_input = input("Enter the numerator: ")
denominator_input = input("Enter the denominator: ")

# TODO: wrap the risky operations in a try/except block
numerator = 0
try:
    numerator = int(numerator_input)
except:
    print("Numerator is not valid")
    quit()
denominator = 0
try:
    denominator = int(denominator_input)
except:
    print("Denominator is not valid")
    quit()

if (denominator == 0):
    print("Denominator cannot be zero")
    quit()
answer = numerator / denominator
print(f"The answer is: {answer}")
# TODO: convert the values to integers and perform the division
# TODO: print clear feedback when something goes wrong
# TODO: only show the answer when the division succeeds
