with open("C:\\Users\\825949\\Documents\\Intro to Programming\\IntroToProgramming\\Assignments\\WheresWaldo\\names.txt","r") as file:
    lines = file.readlines()
    
names = ["waldo", "Carmen", "Odlaw"]

for name in names:
    found = False

    for index, line in enumerate(lines, start=1):
        if name.casefold() in line.casefold():
            print(name.title() + " was found on line " + str(index) + "!")
            found = True
            
if not found:
    print(name.title() + " was not found...")