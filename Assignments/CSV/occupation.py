import csv


with open("C:\\Users\\825949\\Documents\\Intro to Programming\\IntroToProgramming\\Assignments\\CSV\\occupation-2018-census-csv.csv", "r", encoding="utf-8") as file:
    table = csv.DictReader(file)

    occupations = []
    people = []
    codes = []

    for row in table:
        occupations.append(row["Occupation"])

        people.append(int(row["Employed_census_usually_resident_population_count_aged_15_years_and_over"]))

        codes.append(row["Code"])


print("The most common occupation in the US in 2018 was " + occupations[people.index(max(people))] + " with " + str(max(people)) + " people employed in that occupation.")

print("The least common occupation in the US in 2018 was " + occupations[people.index(min(people))] + " with " + str(min(people)) + " people employed in that occupation.")

print("In 2018, there were " + str(people[occupations.index("Grape Grower")]) + " Grape Growers in the US.")

print("In 2018, there were 14298 people employed as " + occupations[people.index(14298)] + "s in the US.")

print("In 2018 the job " + occupations[codes.index("451311")] + " had the code 451311")

