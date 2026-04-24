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

    else:
        print("Invalid choice. Please choose 1, 2, or 3.")
        sit_on_rock()


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
        walk_away()

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

    else: 
        print("Invalid choice. Please choose 1 or 2.")
        left_cave_path()


def right_cave_path():
    print("You take a right into a glowing tunnel.")
    print("You are fascinated in it's shine. So fascinated that you don't notice the drop.")
    print("Game Over.")

    
def climb_down():
    print("You slowly make your way, scaling down a steep path to the bottom of the waterfall.")
    print("You make sure to carefully take each step.")
    print("But...")
    print("You take a wrong step and slip on a rock.")
    print("Though the fall was kind of peaceful, you didn't make it.")
    print("Game Over.")


def enjoy_view():
    print("You decide to sit on the edge of the cliff with your feet in the water.")
    print("You breath in the fresh air and take it all in.")
    print("You are thankful for this life.")
    print("Congrats! You win!")


def jump():
    print("With a running start, you jump off the edge.")
    print("That was just stupid.")
    print("Game Over.")


def scream_and_shake():
    print("You scream like a little girl and rapidly shake your hand around.")
    print("You pause to examine the bite, and see that it is starting to swell.")
    print("A large purple bump forms and you begin to feel dizzy.")
    print("You pass out and unfortunately hit your head on a rock.")
    print("Game Over.")


def gently_remove():
    print("You calmly lift the caterpillar off of your hand and see a bump forming.")
    print("He looks back at you with what appears to be a smile.")
    print("He says, 'Dip your hand in the water.'")
    print("You do, and the bump disappears.")
    print("You've made a friend.")
    print("Congrats! You win!")

def ignore_caterpillar():
    print("You allow the caterpillar to continue walking on your arm.")
    print("He bites you three more times.")
    print("The bite spots swell up into giant purple bumps.")
    print("You begin to feel dizzy.")
    print("You pass out and unfortunately hit your head on a rock.")
    print("Game Over.")


def climb_tree():
    print("Excited, you hastily climb a tree.")
    print("Without paying attention, you miss a branch.")
    print("You fall, hitting every branch on the way down.")
    print("Game Over.")


def explore_garden():
    print("You decide to try another fruit, wondering what ability you'll get next.")
    print("You pick up a tiny watermelon and pop the whole thing into your mouth.")
    print("You wait until you feel your stomach bubble up.")
    print("Game Over.")


def nearest_town():
    print("He gives you a ride to the nearest town.")
    print("His house is on the way, and he says he has to make a pit stop.")
    print("You scrambles into his house, and is gone for about 15 minutes.")
    print("What should you do?")
    print("1. Steal the car.")
    print("2. Knock on his door.")

    nearest_town_choice = input(">>>")

    if nearest_town_choice == "1":
        steal_car()

    elif nearest_town_choice == "2":
        knock_on_door()

    else: 
        print("Invalid choice. Please choose 1 or 2.")
        nearest_town()


def end_of_river():
    print("He gives you a ride to the end of the river.")
    print("You thank him for the ride, and jump into the river.")
    print("You swim into the sunset.")
    print("Congrats! You win!")
    

def free_her():
    print("You attempt to free her, but the tree branch won't come free.")
    print("You decide to cut the branch.")
    print("The branch snaps in two and the girl jumps up.")
    print("She gives you a hug and rans away.")
    print("Congrats! You win!")


def walk_with_her():
    print("You take her hand and say, 'It'll be okay.'")
    print("She says, 'I know.'")
    print("You look away, slightly confused.")
    print("But then, she eats you whole.")
    print("Game Over.")


def open_tomb():
    print("You slowly slide off the cover, and hear a groan from inside.")
    print("A mummy rises up and looks at you.")
    print("He asks, 'Have you come to hear my story?")
    print("What do you say?")
    print("1. Yes.")
    print("No.")

    open_tomb_choice = input(">>>")

    if open_tomb_choice == "1":
        yes_tomb()

    elif open_tomb_choice == "2":
        no_tomb()

    else:
        print("Invalid choice. Please choose 1 or 2.")
        open_tomb()


def steal_gold():
    print("You reach for the gold, but there seems to be some sort of shield.")
    print("A mummy rises from the tomb and yells, 'You are done.'")
    print("You are disintegrated in a second.")
    print("Game Over.")


def steal_car():
    print("You slide into the driver's seat and shift gears.")
    print("But, you realize there aren't any keys.")
    print("He sees, and kicks you out of the car.")
    print("You are lost. Game Over.")


def knock_on_door():
    print("You decide to knock on the door.")
    print("A stranger opens the door, and says, 'Would you like to come in?'")
    print("Do you enter?")
    print("1. Yes")
    print("2. No")

    knock_on_door_choice = input(">>>")

    if knock_on_door_choice == "1":
        enter_door()

    elif knock_on_door_choice == "2":
        dont_enter()

    else:
        print("Invalid Choice. Please choose 1 or 2.")
        knock_on_door()


def yes_tomb():
    print("You say, 'I would like to hear your story.'")
    print("The mummy smiles with rotten teeth.")
    print("He tells his story and you learn from his wisdom.")
    print("You live a long healthy life.")
    print("Congrats! You win!")


def no_tomb():
    print("You say, 'No, thank you.'")
    print("The mummy frowns at you and reaches for your neck.")
    print("The mummy curses you for life.")
    print("Game Over.")


def enter_door():
    print("You enter their small cottage and are met with an comforting home.")
    print("You end up speaking for hours.")
    print("The couple ends up adopting you and taking you in as their own.")
    print("Congrats! You win a long, healthy life.")


def dont_enter():
    print("You say, 'No, thanks. I'll find my way home.'")
    print("The stranger says, 'Be careful.'")
    print("While trying to be independent, you get lost.")
    print("Game Over.")

start_game()