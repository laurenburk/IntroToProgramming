with open("C:\\Users\\825949\\Documents\\Intro to Programming\\IntroToProgramming\\Assignments\\WheresWaldo\\names.txt","r") as file:
    lines = file.readlines()

    found = False

for line in lines:
    if "waldo" in line.lower():
        found = True
        break

if found:
    print("Waldo was found on line " + str(lines.index(line) + 1) + "!")

else:    
    print("Waldo was not found...")