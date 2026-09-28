"""
Portfolio Task - Week 1
By submitting this code you are declaring that all work in this file, other than any provided template code, was written and developed by you independently.
Name: 
"""

name = input("What is your name? ")
print(f"Welcome to LeedsBank's savings calculator {name}!")


# Ask the user to input an amount they want to save every month - this should be an integer.
monthlySavings = input("Enter your monthly savings amount: ")
if(not isinstance(monthlySavings,int))
{
    print("Invalid amount")
    end #we are ending immediately as part of the task
}
# Validate that they have entered an integer.


# Calculate the total amount of money they will have saved by the end of the year (amount per month multiplied by 12).
subtotalSavings = monthlySavings * 12
print(f"You will have saved £{subtotalSavings} by the end of the year")
# print this out for the user with a suitable message.


# Calculate the total amount of money including interest (0.8% of the final annual amount) they will have saved in a year.
totalSavings = subtotalSavings * 1.08
print(f"With interest, you will have £{"{:.2f}".format(totalSavings.format})")
# print this out in the format £X.XX (to two decimal places).

