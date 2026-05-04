#print a countdown
numbers_countdown = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

for numbers in numbers_countdown:
    print(numbers)


#Sum of a list
numbers_add = [2, 6, 77, 4, 2, 3, 64, 9, 33, 21]
total = 0
for num in numbers_add:
    total += num
print(total)


#Square Each Number
numbers_square = [1, 2, 3, 4, 5]
squares = []
for num in numbers_square:
    squares.append(num ** 2)
print(squares)


#Character Count
enter_string = input("Please enter a string\n>>>")
vowels = ["a", "e", "i", "o", "u"]
vowel_total = 0

for char in enter_string:
    if char in vowels:
        vowel_total += 1
print(str(vowel_total) + " Vowels")


#Print Multiplication Table
number_mult = int(input("Please enter a number\n>>>"))

for i in range(1, 11):
    print(f"{number_mult} x {i} = {number_mult * i}")


#List of Names
names = ["Lauren", "Ronin", "Ellie", "Parker", "Will"]

for names in names:
    print("Hello, " + names + "!")