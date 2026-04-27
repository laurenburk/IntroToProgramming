favorite_fruit = ["tomato", "strawberry", "blackberry", "apple", "banana"]

print(favorite_fruit[0], favorite_fruit[-1])

favorite_fruit.append(input("Please add another fruit\n>>>"))

print(favorite_fruit[0], favorite_fruit[1], favorite_fruit[2], favorite_fruit[3], favorite_fruit[4], favorite_fruit[5])

favorite_fruit.remove(input("Which fruit would you like to remove?\n>>>"))

print(favorite_fruit[0], favorite_fruit[1], favorite_fruit[2], favorite_fruit[3], favorite_fruit[4])

favorite_fruit.sort()

print(favorite_fruit[0], favorite_fruit[1], favorite_fruit[2], favorite_fruit[3], favorite_fruit[4])

fruits = ["tomato", "tomato", "orange", "blackberry", "tomato", "apple"]

tomato_count = fruits.count("tomato")

print(tomato_count, "tomatoes")