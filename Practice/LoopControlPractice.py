#break at 15
for i in range(1,20):
    if i == 16:
        break
    print(i)


#print odd numbers
for i in range(1, 30):
    if i % 2 == 0:
        continue
    print(i)


#implement loop with pass
for i in range(5):
    if i == 2:
        pass  # Placeholder for future code
    print(i)



#countdown skip 5
for i in range(10, 0, -1):
    if i == 5:
        continue
    print(i)

numbers = [3, 5, 6, 3, 7, -6, 9, 1]
total = 0
for num in numbers:
    if num < 0:
        break
    total += num
    print(total)