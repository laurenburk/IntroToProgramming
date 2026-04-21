name = input("What is your name? >>> ")

def start_game():
    print("The sun shines brightly in your eyes as you lay on soft grass.")
    print("You look around and see a beautiful meadow with colorful flowers and a clear blue sky.")
    print("You see three paths, each leading in a different direction. Which path do you choose?")
    print("1. The left path, which is lined with flowers and seems peaceful.")
    print("2. The middle path, which is dark and mysterious.")
    print("3. The right path, which is rocky and steep.")

    path_choice = input(">>> ")

    if path_choice == "1":
        flower_path()

    elif path_choice == "2":
        dark_path()

    elif path_choice == "3":
        rocky_path()

    else:
        print("Invalid choice. Please choose 1, 2, or 3.")
        start_game()


def flower_path():
    print("You walk down the flower path, enjoying the sweet scent of the blossoms.")
    print("As you walk further, you see a river with a rickety bridge.")
    print("What do you do?")
    print("1. Cross the bridge.")
    print("2. Follow the river upstream.")
    print("3. Sit by the river and relax.")

    flower_path_choice = input(">>> ")

    if flower_path_choice == "1":
        cross_bridge()

    elif flower_path_choice == "2":
        follow_river()

    elif flower_path_choice == "3":
        relax_by_river()

    else:
        print("Invalid choice. Please choose 1, 2, or 3.")
        flower_path()


def dark_path():
    print("You walk down the dark path, feeling a chill in the air.")
    print("As you walk further, you hear a voice calling your name.")
    print("What do you do?")
    print("1. Look for the source of the voice.")
    print("2. Call out, 'Who is this?'")
    print("3. Stay silent.")

    dark_path_choice = input(">>> ")

    if dark_path_choice == "1":
        look_for_voice()

    elif dark_path_choice == "2":
        call_out_who()

    elif dark_path_choice == "3":
        stay_silent()

    else:
        print("Invalid choice. Please choose 1, 2, or 3.")
        dark_path()


def rocky_path():
    print("You walk down the rocky path, struggling to keep your footing.")
    print("As you walk further, you see a cave entrance.")
    print("What do you do?")
    print("1. Enter the cave.")
    print("2. Keep walking past the cave.")
    print("3. Sit on a rock and catch your breath.")

    rocky_path_choice = input(">>> ")

    if rocky_path_choice == "1":
        enter_cave()

    elif rocky_path_choice == "2":
        keep_walking()

    elif rocky_path_choice == "3":
        sit_on_rock()

    else:
        print("Invalid choice. Please choose 1, 2, or 3.")
        rocky_path()


def cross_bridge():
    print("You slowly make your way across the rickety bridge, holding onto the ropes for support.")
    print("On the other side, you are met with a garden full of magical fruit.")
    print("Which fruit do you choose to eat?")
    print("1. The giant pear.")
    print("2. The purple banana.")
    print("3. The glowing apple.")

    cross_bridge_choice = input(">>> ")

    if cross_bridge_choice == "1":
        eat_pear()

    elif cross_bridge_choice == "2":
        eat_banana()

    elif cross_bridge_choice == "3":
        eat_apple()

    else:
        print("Invalid choice. Please choose 1, 2, or 3.")
        cross_bridge()


def follow_river():
    print("As you walk alongside the river, you see a small boat tied to a tree.")
    print("Out from the forest, a small man appears.")
    print("'Hello there,' he says. 'Would you like a ride down the river?'")
    print("What do you do?")
    print("1. Accept the ride.")
    print("2. Politely decline and keep walking.")

    follow_river_choice = input(">>> ")

    if follow_river_choice == "1":
        accept_ride()

    elif follow_river_choice == "2":
        decline_ride()

    else:
        print("Invalid choice. Please choose 1 or 2.")
        follow_river()


def relax_by_river():
    print("You sit by the river, taking a deep breath in.")
    print("As you lay in the sun, you hear a faint scream coming from the forest.")
    print("What do you do?")
    print("1. Investigate the scream.")
    print("2. Go look for help before investigating.")
    print("3. Ignore the scream and continue relaxing.")

    relax_by_river_choice = input(">>> ")

    if relax_by_river_choice == "1":
        investigate_scream()

    elif relax_by_river_choice == "2":
        look_for_help()

    elif relax_by_river_choice == "3":
        ignore_scream()

    else:
        print("Invalid choice. Please choose 1, 2, or 3.")
        relax_by_river()


def look_for_voice():
    print("You look around the bushes, searching for the source of the voice.")
    print("Suddenly, a young girl jumps out and say, 'HI!'")
    print("She says, 'Can you help me find my way home?'")
    print("What do you do?")
    print("1. Take her hand and say, 'Sure, let's go!'")
    print("2. Say, 'Sorry, I can't help you.' and walk away.")
    print("3. Ask, 'Where do you live?'")

    look_for_voice_choice = input(">>> ")

    if look_for_voice_choice == "1":
        help_the_girl()

    elif look_for_voice_choice == "2":
        walk_away()

    elif look_for_voice_choice == "3":
        ask_where_live()

    else:
        print("Invalid choice. Please choose 1, 2, or 3.")
        look_for_voice()


