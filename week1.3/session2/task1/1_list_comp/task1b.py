# Week 1.3, Session 1: Task 6b

values = [1,4,2,6,3,7]

print(values)

newval = []
for i in values:
    if i % 2 == 0:
        newval.append(2 * i)
    else:
        newval.append(i)

print(newval)

# write the list comprehension equivalent to the `for` loop
newval2 = [values[x] * 2 if x % 2 == 0 else values[x] for x in range(0,len(values))]
print(newval2)

