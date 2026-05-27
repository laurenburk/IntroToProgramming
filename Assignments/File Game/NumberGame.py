with open("C:\\Users\\825949\\Documents\\Intro to Programming\\IntroToProgramming\\Assignments\\File Game\\scores.txt", "a") as file:

    import random

def display_leaderboard():
    pass

def play_game():
    display_leaderboard()
    name = input("ENTER YOUR NAME\n> ")
    target = random.randrange(1,1001)
    guess = 0
    num_guesses = 0

    while guess != target:
        guess = int(input("ENTER A NUMBER\n> "))
        num_guesses += 1

        if guess < target:
            print("LOW")

        elif guess > target:
            print("HIGH")

    print("CORRECT! THE NUMBER WAS " + str(target))

    with open("C:\\Users\\825949\\Documents\\Intro to Programming\\IntroToProgramming\\Assignments\\File Game\\scores.txt", "a") as file:
        file.write("\n" + name + "," + str(num_guesses))
        file.close()

    play_again = input("PLAY AGAIN?\n[y/n]\n> ")
    if play_again == "y":
        play_game()

play_game()