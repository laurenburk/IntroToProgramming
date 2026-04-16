shoes_untied = True
preoccupied = False
print(not shoes_untied and not preoccupied)

#nested if statement
age = int(input("Enter your age: "))
has_permission = True

if age >= 18:
    if has_permission:
        print("Access Granted")

    else:
        print("Access Denied: Permission Required")

else:
    print("Access Denied: Age Restriction")

def even_or_odd(number):
    if number % 2 == 0:
        return "Even"
    
    else:
        return "Odd"
    
even_or_odd()