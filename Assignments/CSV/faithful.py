import csv


with open("C:\\Users\\825949\\Documents\\Intro to Programming\\IntroToProgramming\\Practice\\CSV\\faithful.csv", "r") as file:
    table = csv.DictReader(file)

    wait_times = []
    length_times = []
    total_length = 0
    total_wait = 0
    rows = 0


    for row in table:
        wait_times.append(row["Wait"])
        length_times.append(row["Length"])
        total_wait += int(row["Wait"])
        total_length += float(row["Length"])
        rows += 1

        max_wait = max(wait_times)

    print("The average eruption length was " + str(total_length / rows) + " minutes.")
    print("The longest eruption length was " + str(max(length_times)) + " minutes.")
    print("The shortest eruption length was " + str(min(length_times)) + " minutes.")

    print("The average wait time was " + str(total_wait / rows) + " minutes.")
    print("The shortest wait time was " + str(min(wait_times)) + " minutes.")
    print("The longest wait time was " + str(max(wait_times)) + " minutes.")
    
    print("the eruption length for the longest wait time was " + str(length_times[wait_times.index(max_wait)]) + " minutes.")



    