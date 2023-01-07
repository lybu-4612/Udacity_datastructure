limit = int(input("Enter the limit of the list"))

Odd_nums = []

for i in range(1, limit):
    if i % 2 != 0:
        Odd_nums.append(i)

print(Odd_nums)