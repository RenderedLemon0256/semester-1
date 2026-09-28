"""Advanced Task 4: Deadline Breakdown
- Ask how many minutes remain until an assignment deadline.
- Use integer division and modulo to convert this number into days, hours, and minutes.
- Present the result using a formatted string such as "2 days, 3 hours, 15 minutes remaining".
- Extension: handle negative input by printing a warning that the deadline has already passed.
"""

minutes_remaining_input = input("Minutes remaining until the deadline: ")
totalMinutes = int(minutes_remaining_input)
if(totalMinutes <= 0):
    print("Deadline has passed")
    quit()

totalHours = totalMinutes // 60
remainingMinutes = totalMinutes - (totalHours * 60)
totalDays = totalHours // 24
remainingHours = totalHours - (totalDays * 24)

print(f"{totalDays} days, {remainingHours} hours, {remainingMinutes} minutes remaining")

# TODO: convert the input to an integer
# TODO: calculate whole days, leftover hours, and remaining minutes
# TODO: print the breakdown using f-strings
# Extension: detect negative values and print a warning instead
