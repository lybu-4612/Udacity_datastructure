expenses = [2200, 2350, 2600, 2130, 2190]

sol1 = expenses[1] - expenses[0]
print(sol1)
sol2 = expenses[0] + expenses[1] + expenses[2]
print(sol2)

for i in expenses:
    if i == 2000:
        sol3 =  True
    else:
        sol3 =  False

print (sol3)

expenses.append(1980)

print(expenses)

expenses[3] += 200

print(expenses)
