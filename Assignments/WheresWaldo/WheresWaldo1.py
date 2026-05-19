with open("C:\\Users\\825949\\Documents\\Intro to Programming\\IntroToProgramming\\Assignments\\WheresWaldo\\names.txt","r") as file:
    lines = file.readlines()

    found = False

for line in lines:
    if "Waldo" in line:
        found = True
        break

if found:
    print("Waldo was found!")

else:    
    print("Waldo was not found...")