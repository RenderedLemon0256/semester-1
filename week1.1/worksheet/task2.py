
#Portfolio Task - Week 1
#By submitting this code you are declaring that all work in this file, other than any provided template code, was written and developed by you independently.
#Name: 
try:
    # Ask the user to input an amount they want to save every month - this should be an integer.
    monthlySavingsInput = input("Enter your monthly savings amount: ")

    # Validate that they have entered an integer.


    # Calculate the total amount of money they will have saved by the end of the year (amount per month multiplied by 12).
    subtotalSavings = int(monthlySavingsInput) * 12
    print(subtotalSavings)
    # print this out for the user with a suitable message.


    # Calculate the total amount of money including interest (0.8% of the final annual amount) they will have saved in a year.
    totalSavings = subtotalSavings * 1.008
    print("£" + "{:.2f}".format(totalSavings))
    # print this out in the format £X.XX (to two decimal places).
except:
    print("Invalid amount")
