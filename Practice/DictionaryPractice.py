#Create a Dictionary and print
grades_dict = {
    "Alice": "A",
    "Bob": "B",
    "Charlie": "C",
    "David": "A",
    "Eve": "B"
}

#Accessing Values
student = {"name": "Alice", "age": 16, "grade": "A"}

print(student["name"], student["age"])

#Updating Values
grades_dict["Alice"] = "A+"

for key, value in grades_dict.items():
    print(f"{key}: {value}")


#Adding New Key-Value Pairs
movie_dict = {
    "Pulp Fiction": "1994",
    "Fight Club": "1999",
    "Wall-E": "2008"
}
print("Pick a movie:")
movie_dict[input("What movie did you pick?\n>>>")] = input("What year did your chosen movie come out?\n>>>")

print(movie_dict)

#Removing Key-Value Pairs
fruits_dict = {"banana": "$2", "apple": "$1", "orange": "$5", "grape": "$3"}

print(fruits_dict)

print("Which fruit would you like to get rid of?")

del fruits_dict[input(">>>")]

print(fruits_dict)

#Looping Through a Dictionary
inventory = {"apples": 10, "bananas": 5, "oranges": 8}

for key, value in inventory.items():
    print(f"{key}: {value}")

#Counting Occurrences



#Nested Dictionaries
books_dict = {
    
    "AQWF": {
        "title": "All Quiet on the Western Front",
        "author": "Erich Maria Remarque",
        "publication": "1928"
    },

    "NCFOM": {
        "title": "No Country for Old Men",
        "author": "Cormac McCarthy",
        "publication": "2005"
    },

    "TGG": {
        "title": "The Great Gatsby",
        "author": "F. Scott Fitzgerald",
        "publication": "1925"
    },

}

print(books_dict["AQWF"])
print(books_dict["NCFOM"])
print(books_dict["TGG"])

#Dictionary Comprehension
squares = {x: x**2 for x in range(1,11)}

print(squares)

salaries_dict = {
    
    "Alice_dict": {
        "salary": 120000,
    },

    "bob_dict": {
        "salary": 100000,
    },

    "Charlie_dict": {
        "salary": 20000,
    },

    "David_dict": {
        "salary": 50000,
    }

}
