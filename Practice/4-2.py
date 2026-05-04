fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)


for letter in "hello":
    print(letter)


for i in range(5):
    print(i)


numbers = [2, 4, 6, 8]
total = 0
for num in numbers:
    total += num
print(total)

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

for row in matrix:
    for item in row:
        print(item, end=" ")
    print()


# Using break
for i in range(5):
    if i == 3:
        break
    print(i)


# Using continue
for i in range(5):
    if i == 3:
        continue
    print(i)