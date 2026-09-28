"""Advanced Task 1: Trip Planner
- Ask for a destination name, total distance in miles, and planned travel time in hours.
- Convert the numeric inputs so you can calculate an approximate average speed for the journey.
- Display a human-readable summary that includes the destination and the speed formatted to two decimal places.
- Extension: warn if either numeric value is zero or negative.
"""

destination = input("Where are you going to? ")

distance_miles_input = input("How many miles will you travel? ")
time_hours_input = input("How many hours will the journey take? ")

# TODO: convert distance_miles_input and time_hours_input to numbers
try:
    distanceMiles = float(distance_miles_input)
    timeHours = float(time_hours_input)
except:
    print("Invalid input")
    quit()
# TODO: calculate the average speed in miles per hour
if(timeHours <= 0):
    print(f"Inputted hours: {timeHours} is zero or negative")
    quit()
averageSpeed = distanceMiles/timeHours
# TODO: print a summary message using an f-string
print(f"You are going to {destination}, {"{:.1f}".format(distanceMiles)} miles away. It will take {"{:.1f}".format(timeHours)} hours and you will travel at an average speed of {"{:.2f}".format(averageSpeed)}mph")
# Extension: add validation for zero or negative values
