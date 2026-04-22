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
    print("2. Call out, 'Who's there?'")
    print("3. Return back the way you came.")

    dark_path_choice = input(">>> ")

    if dark_path_choice == "1":
        look_for_voice()

    elif dark_path_choice == "2":
        call_out_who()

    elif dark_path_choice == "3":
        return_back()

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


def call_out_who():
    print("You call out, 'Who's there?' but there is no response.")
    print("You repeat, 'Who's there?' In a bush, you see a pair of eyes staring at you.")
    print("What do you do?")
    print("1. Approach the bush to see who it is.")
    print("2. Run away as fast as you can.")
    print("3. Shine a flashlight on the bush to see who it is.")

    call_out_who_choice = input(">>> ")

    if call_out_who_choice == "1":
        approach_bush()

    elif call_out_who_choice == "2":
        run_away()

    elif call_out_who_choice == "3":
        shine_flashlight()

    else:
        print("Invalid choice. Please choose 1, 2, or 3.")
        call_out_who()


def return_back():
    print("Slightly shaken, you decide to return back the way you came.")
    print("Once again, you meet the other two paths.")
    print("Which path do you choose?")
    print("1. The left path, which is lined with flowers and seems peaceful.")
    print("2. The right path, which is rocky and steep.")

    return_back_choice = input(">>> ")

    if return_back_choice == "1":
        flower_path()

    elif return_back_choice == "2":
        rocky_path()

    else:
        print("Invalid choice. Please choose 1 or 2.")
        return_back()


def enter_cave():
    print("You enter the cave, and hear dripping water echo off the walls.")
    print("As you walk further, you are met with two paths.")
    print("Which path do you choose?")
    print("1. The left path.")
    print("2. The right path.")

    enter_cave_choice = input(">>> ")

    if enter_cave_choice == "1":
        left_cave_path()

    elif enter_cave_choice == "2":
        right_cave_path()

    else:
        print("Invalid choice. Please choose 1 or 2.")
        enter_cave()


def keep_walking():
    print("You keep walking past the cave, and find yourself at the edge of a cliff.")
    print("As you look down, you see a beautiful waterfall.")
    print("What do you do?")
    print("1. Carefully climb down the cliff.")
    print("2. Sit on the edge and enjoy the view.")
    print("3. Jump.")

    keep_walking_choice = input(">>> ")

    if keep_walking_choice == "1":
        climb_down()

    elif keep_walking_choice == "2":
        enjoy_view()

    elif keep_walking_choice == "3":
        jump()

    else:
        print("Invalid choice. Please choose 1, 2, or 3.")
        keep_walking()


def sit_on_rock():
    print("You sit on a rock, and a caterpillar crawls up your leg.")
    print("It looks up at you and then out of nowhere, it bites you.")
    print("What do you do?")
    print("1. Scream in pain and try to shake the caterpillar off.")
    print("2. Stay calm and try to gently remove the caterpillar.")
    print("3. Ignore the caterpillar and continue sitting.")

    sit_on_rock_choice = input(">>> ")
    
    if sit_on_rock_choice == "1":
        scream_and_shake()

    elif sit_on_rock_choice == "2":
        gently_remove()

    elif sit_on_rock_choice == "3":
        ignore_caterpillar()


def eat_pear():
    print("Slowly, you chomp down the giant pear.")
    print("As you eat, you feel a strange sensation in your body.")
    print("All of a sudden, you whole body turns GREEN!")
    print("You must now live your life like this forever.")
    print("Game Over. Sorry.")


def eat_banana():
    print("You take a bite of the purple banana.")
    print("As you eat, you feel a surge of energy coursing through your body.")
    print("You suddenly feel incredibly strong and agile!")
    print("What do you do?")
    print("1. Test out your new strength and agility by climbing a nearby tree.")
    print("2. Use your new abilities to explore the garden and see what other magical things you can find.")

    eat_banana_choice = input(">>> ")
    
    if eat_banana_choice == "1":
        climb_tree()

    elif eat_banana_choice == "2":
        explore_garden()

    else:
        print("Invalid choice. Please choose 1 or 2.")
        eat_banana()


def eat_apple():
    print("You take a bite of the glowing apple.")
    print("As you eat, you start to feel funny...")
    print("The apple is poisonous! You start to feel dizzy and weak.")
    print("You collapse to the ground and everything goes black.")
    print("Game Over.")


def accept_ride():
    print("You accept the ride and get into the boat with the small man")
    print("As you float down the river, the man asks, 'Where to?'")
    print("What do you say?")
    print("1. 'Take me to the nearest town.'")
    print("2. 'Take me to the end of the river.'")

    accept_ride_choice = input(">>> ")

    if accept_ride_choice == "1":
        nearest_town()

    elif accept_ride_choice == "2":
        end_of_river()

    else:
        print("Invalid choice. Please choose 1 or 2.")
        accept_ride()


def decline_ride():
    print("You politely decline the ride and the man's smile fades.")
    print("As you continue walking, you can feel his eyes on you.")
    print("Suddenly, you feel a hand grab your arm.")
    print("The man pushes you into the river.")
    print("You struggle to swim to the shore, but the current is too strong.")
    print("Game Over.")


def investigate_scream():
    print("You decide to investigate the scream and head towards the forest.")
    print("As you walk deeper into the woods, you see a figure tied to a tree.")
    print("It's a young girl.")
    print("She looks up at you with tears in her eyes and says, 'Please help me!'")
    print("What do you do?")
    print("1. Help free her.")
    print("2. Walk away.")

    investigate_scream_choice = input(">>> ")
    
    if investigate_scream_choice == "1":
        free_her()

    elif investigate_scream_choice == "2":
        walk_away_from()

    else:
        print("Invalid choice. Please choose 1 or 2.")
        investigate_scream()


def look_for_help():
    print("You decide to look for help before investigating the scream.")
    print("As you walk back towards the meadow, you see a group of people having a picnic.")
    print("You approach them and explain the situation.")
    print("They agree to help you investigate the scream, and you search together.")
    print("You find a girl with her foot stuck in a branch.")
    print("As a team, you free her.")
    print("Congrats! You win!")


def ignore_scream():
    print("You decide to ignore the scream. You figure someone else will help.")
    print("Merrily you roll along, no cares in the world.")
    print("You didn't win or lose. You may want to help next time.")


def help_the_girl():
    print("You take the girls hand and ask, 'What's your mother's name?'")
    print("The girl doesn't respond.")
    print("You look down at her and she has a creepy smile on her face.")
    print("Within a second, she eats you whole.")
    print("Game Over.")


def walk_away():
    print("You say, 'Sorry, I can't help.'")
    print("The girl begins to cry, and says, 'You are evil.'")
    print("Within a second, she eats you whole.")
    print("Game Over.")


def ask_where_live():
    print("You ask her, 'Where do you live?'")
    print("She points at a dark forest.")
    print("What do you do?")
    print("1. Walk with her.")
    print("2. Walk away.")

    ask_where_live_choice = input(">>>")

    if ask_where_live_choice == "1":
        walk_with_her()

    elif ask_where_live_choice == "2":
        walk_away()

    else: 
        print("Invalid choice. Please choose 1 or 2.")
        ask_where_live()


def approach_bush():
    print("You slowly make your way towards the bush.")
    print("You begin to feel your way through the leaves.")
    print("All of a sudden, a grey bunny hops out and onto your chest.")
    print("You found a new bestfriend.")
    print("Congrats! You win!")


def run_away():
    print("You begin to sprint in the opposite direction.")
    print("You look back at the bush, and see a giant rabbit runnng towards you.")
    print("In one chomp, the rabbit eats you whole.")
    print("Game Over.")


def shine_flashlight():
    print("You take out your handy dandy flashlight and point it towards the bush.")
    print("You see a baby bunny looking back at you.")
    print("You say, 'Awww.'")
    print("But then, the mama appears. She is 100x the size of the baby.")
    print("In one chomp, the mama eats you whole.")
    print("Game Over.")


def left_cave_path():
    print("You take a left into a narrow and dark tunnel.")
    print("You discover a tomb surrounded with gold.")
    print("What do you do?")
    print("1. Open the tomb.")
    print("2. Steal the gold surrounding the tomb.")

    left_cave_path_choice = input(">>>")

    if left_cave_path_choice == "1":
        open_tomb()

    elif left_cave_path_choice == "2":
        steal_gold()


def right_cave_path():
    print("You take a right into a glowing tunnel.")
    print("You are fascinated in it's shine. So fascinated that you don't notice the drop.")
    print("Game Over.")

    

start_game()