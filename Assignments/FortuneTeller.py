print("Today you will learn about your fortune! Answer the following questions to find out what your future holds!")

def fortune():
    try:
        age = int(input("How old are you?->"))

        siblings = int(input("How many siblings do you have?->"))

        lucky_number = int(input("What is your lucky number between 1 and 30?->"))
       
        if age < 18 and siblings == 0 and lucky_number <= 10:
            print("You will be a famous singer!")

        elif age < 18 and siblings >= 0 and lucky_number > 10 and lucky_number <= 20:
            print("You will be a famous athlete!")

        elif age <18 and siblings == 0 and lucky_number > 20 and lucky_number <= 30:
            print("You will get in a car crash soon...")

        elif age < 18 and siblings == 1 and lucky_number <= 20:
            print("You will have a pet anteater!")

        elif age < 18 and siblings >= 2 and lucky_number <= 30:
            print("You will live to 120 years old!")

        elif age > 18 and siblings == 0 and lucky_number <= 10:
            print("You will be a famous actor!")

        elif age > 18 and siblings >= 3 and lucky_number > 10 and lucky_number <= 20:
            print("You will be a famous chef!")

        elif age > 18 and siblings >= 1 and lucky_number > 20 and lucky_number <= 30:
            print("You will be a successful entrepreneur!")

        elif age > 18 and siblings >= 2 and lucky_number < 10:
            print("You will be a famous scientist!")
    except ValueError:
        print("Please enter a valid input!")
    
print(fortune())