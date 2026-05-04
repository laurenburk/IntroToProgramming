import random

user_input = None

secret_number = random.randint(1, 100)

while user_input != secret_number:
    try:
        user_input = int(input("Guess the Number between 1 and 100!: "))
        
        if user_input > secret_number:
            print("The number is smaller! Try again.")
        elif user_input < secret_number:
            print("The number is bigger! Try again.")
        else:
            print("That is the correct number!")

    except ValueError:
        print("Please enter a valid whole number.")
