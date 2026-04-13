answer_one = input("How many cards are in a standard deck of playing cards?\n->")

if (answer_one == "52"):
    print("You are very smart! That is correct!")
else:
    print("That is incorrect. The correct answer is 52.")

answer_two = input("What is the name of John Travolta's character in the movie 'Pulp Fiction'?\n->")

if (answer_two == "Vincent Vega"):
    print("You are very smart! That is correct!")
else:
    print("That is incorrect. The correct answer is Vincent Vega.")

answer_three = input("Which country is the largest in the world?\n->")

if (answer_three == "Russia"):
    print("You are very smart! That is correct!")
else:
    print("That is incorrect. The correct answer is Russia.")

answer_four = input("What is an eight-sided shape called?\n->")

if (answer_four == "Octagon"):
    print("You are very smart! That is correct!")
else:
    print("That is incorrect. The correct answer is Octagon.")

answer_five = input("What is the name of Elvis Presley's Memphis home?\n->")

if (answer_five == "Graceland"):
    print("You are very smart! That is correct!")
else:
    print("That is incorrect. The correct answer is Graceland.")

def tally_score():
    score = 0
    if (answer_one == "52"):
        score += 1
    if (answer_two == "Vincent Vega"):
        score += 1
    if (answer_three == "Russia"):
        score += 1
    if (answer_four == "Octagon"):
        score += 1
    if (answer_five == "Graceland"):
        score += 1
    return score

print("Your total score is: " + str(tally_score()) + "/5")