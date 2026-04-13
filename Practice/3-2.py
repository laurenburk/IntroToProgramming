diameter = input("What is the diameter of the coin in mm?\n->")
diameter = float(diameter)

if (diameter >= 24.26):
    print("Quarter")

elif (diameter >= 21.21):
    print("Nickel")

elif (diameter >= 19.05):
    print("Penny")

elif (diameter >= 17.91):
    print("Dime")