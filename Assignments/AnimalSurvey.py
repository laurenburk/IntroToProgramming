favorite_animal = input("What is your favorite animal?\n->")
animal_color = input("What color is this animal?\n->")
animal_home = input("Where does this animal usually live?\n->")
animal_teeth = input("Does this animal have dull or sharp teeth?\n->")
animal_special = input("What is something special that your favorite animal can do?\n->")
reason = input("Why do you like this animal?\n->")

def results():
    print("Your favorite animal is a " + favorite_animal + " because " + reason + ".")
    print("This animal can be " + animal_color + ".")
    print(favorite_animal + "s usually live in " + animal_home + ".")
    print("A " + favorite_animal + " has " + animal_teeth + " teeth.")
    print(favorite_animal + "s can " + animal_special)