with open("C:\\Users\\825949\\Documents\\Intro to Programming\\IntroToProgramming\\Assignments\\WheresWaldo\\names.txt","r") as file:
    lines = file.readlines()

    found = False
    
search_name = input("Enter the name you want to search for: ")

for index, line in enumerate(lines, start=1):
    if search_name in line:
        print(f"{search_name} was found on line {index}!")
        found = True

if not found:
    print(f"{search_name} was not found...")