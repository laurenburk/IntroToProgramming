with open("C:\\Users\\825949\\Documents\\Intro to Programming\\IntroToProgramming\\Assignments\\WheresWaldo\\names.txt","r") as file:
    lines = file.readlines()

    found = False
    

for index, line in enumerate(lines, start=1):
    if "waldo" in line.casefold():
        print("Waldo was found on line " + str(index) + "!")
        found = True

if not found:
    print("Waldo was not found...")