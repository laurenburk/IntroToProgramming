num = 4 #global scope

def my_function():
    #local scope

    global num #now is referring to num outside of function, through rest of func, global is referenced
    num = 5

my_function()

print(num)

var = 5

def print_var():
    print(var)

print_var()