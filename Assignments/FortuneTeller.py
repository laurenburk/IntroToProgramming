print("Today you will learn about your fortune! Answer the following questions to find out what your future holds!")
name = input("What is your name?->")
age = int(input("How old are you?->"))
favorite_color = input("What is your favorite color?->")

def fortune():
    if favorite_color == "red":
        return "You may experience love in your future..."
    elif favorite_color == "blue":
        return "You may experience a hardship in your future, but it will make you stronger..."
    elif favorite_color == "green":
        return "You may have a large sum of money in your future..."
    elif favorite_color == "yellow":
        return "You may have a long and happy life in your future..."
    elif favorite_color == "purple":
        return "Relax, you will see your success blossom soon enough..."
    else:
        return "Your future is a mystery, but it will be an interesting one!"
    
print(fortune())