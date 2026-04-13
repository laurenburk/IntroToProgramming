diameter = input("What is the diameter of the coin in mm?\n->")
diameter = float(diameter)

if (diameter >= 24.26):
    print("That is a Quarter")

elif (diameter >= 21.21):
    print("That is a Nickel")

elif (diameter >= 19.05):
    print("That is a Penny")

elif (diameter >= 17.91):
    print("That is a Dime")

else:
    print("Pocket Lint...")