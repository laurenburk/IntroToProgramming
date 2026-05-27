import csv


with open("C:\\Users\\825949\\Documents\\Intro to Programming\\IntroToProgramming\\Assignments\\CSV\\deniro.csv", "r") as file:
    table = csv.DictReader(file)

    movie_years = []
    movie_scores = []
    movie_titles = []
    max_title_length = 0

    for row in table:
        movie_years.append(row["Year"])
        movie_scores.append(int(row["Score"]))
        movie_titles.append(row["Title"])
        if len(row["Title"]) == max(max_title_length, len(row["Title"])):
            max_title_length = len(row["Title"])

    print("The lowest rated movie was " + str(movie_titles[movie_scores.index(min(movie_scores))]) + " with a score of " + str(min(movie_scores)) + ".")
    print("The highest rated movie was " + str(movie_titles[movie_scores.index(max(movie_scores))]) + " with a score of " + str(max(movie_scores)) + ".")
    print("The average score of all the movies was " + str(sum(movie_scores) / len(movie_scores)) + ".")

    print("The movie with the longest name was " + str(movie_titles[movie_titles.index(max(movie_titles, key=len))]) + " with a title length of " + str(max_title_length) + ".")

    