counter = 1
while counter <= 5:
    print(counter)
    counter += 1  # Increment the counter




counter = 1
while counter <= 10:
    print(counter)
    if counter == 5:
        break  # Exit the loop when counter reaches 5
    counter += 1


counter = 0
while counter < 5:
    counter += 1
    if counter == 3:
        continue  # Skip the rest of the loop when counter is 3
    print(counter)



user_input = ""
while user_input.lower() != "exit":
    user_input = input("Enter something (type 'exit' to quit): ")
    print("You entered:", user_input)


i = 1
while i <= 3:
    j = 1
    while j <= 2:
        print(f"i = {i}, j = {j}")
        j += 1
    i += 1