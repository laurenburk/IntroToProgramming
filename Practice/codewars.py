string = input("Enter a string:")
repeat = int(input("How many times do you want to repeat the string?"))

def repeat_string(string, repeat):
    return string * repeat

print(repeat_string(string, repeat))