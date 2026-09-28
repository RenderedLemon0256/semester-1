"""Advanced Task 2: Budget Breakdown
- Ask for three separate expense amounts (for example: travel, food, accommodation).
- Convert each input so you can add them together to get a total trip cost.
- Calculate the average spend per category and show each value with an f-string.
- Extension: format the totals so they always show two decimal places.
"""

travel_cost_input = input("Travel cost in pounds: £")
food_cost_input = input("Food cost in pounds: £")
accommodation_cost_input = input("Accommodation cost in pounds: £")

# TODO: convert each value to a number type that supports decimals
travelCost = float(travel_cost_input)
foodCost = float(food_cost_input)
accommodationCost = float(accommodation_cost_input)
# TODO: calculate the total and the average spend per category
totalCost = travelCost + foodCost + accommodationCost
averageCost = totalCost / float(3)
# TODO: print the three costs, the total, and the average
print(f"Travel Costs: £{"{:.2f}".format(travelCost)}, Food Costs: £{"{:.2f}".format(foodCost)}, Accomodation Costs: £{"{:.2f}".format(accommodationCost)}, Total Cost: £{"{:.2f}".format(totalCost)}, Average Cost per Category: £{"{:.2f}".format(averageCost)}")
# Extension: format the totals to two decimal places
