# Week 1.2, Session 1: Task 5

rivers = {
    "London": "Thames",
    "Leeds": "Aire",
    "Liverpool": "Mersey"
}

print(rivers)

# Add two new entries to the rivers database
rivers["Coleraine"] = "Bann"
rivers["Omagh"] = "Strule"

# Display all the keys
for city in rivers.keys():
    print(city)

# Display all the values
for river in rivers.values():
    print(river)

# Display all the key:value pairs, as tuples
for pair in rivers.items():
    print(pair)

# Delete an entry from the rivers database
rivers.pop("Leeds")