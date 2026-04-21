name = input("What is your name? >>>")

def start_game():
    print("You wake up in the middle of the night. You hear someone call out your name. You live alone. What do you do?")
    print("1. Call out, 'Hello?'")
    print("2. Stay Silent. Don't Move a Muscle.")
    print("3. Hide under the bed.")

    start_game_choice = input(">>>")
    
    if start_game_choice == "1":
        call_out_hello()

    elif start_game_choice == "2":
        stay_silent()

    elif start_game_choice == "3":
        hide_under_bed()

    else:
        print("Invalid choice. Please choose 1, 2, or 3.")
        start_game()


def call_out_hello():
    print("You call out, 'Hello?' but there is no response. What do you do?")
    print("1. Call out again, louder this time.")
    print("2. Leave the room and look for the source of the voice.")

    call_out_hello_choice = input(">>>")

    if call_out_hello_choice == "1":
        call_out_again()

    elif call_out_hello_choice == "2":
        leave_the_room()

    else:
        print("Invalid choice. Please choose 1, 2, or 3.")
        call_out_hello()


def stay_silent():
    print("You sit silently in your bed, shaking. The voice calls out again, louder and angrier this time. What do you do?")
    print("1. Close your eyes and go back to sleep.")
    print("2. Get out of bed and grab a weapon.")
    print("3. Call 911.")

    stay_silent_choice = input(">>>")

    if stay_silent_choice == "1":
        close_eyes()

    elif stay_silent_choice == "2":
        grab_weapon()

    elif stay_silent_choice == "3":
        call_911()

    else:
        print("Invalid choice. Please choose 1, 2, or 3.")
        stay_silent()


def hide_under_bed():
    print("You quickly hide under your bed. You hear footsteps getting louder and louder. The voice is getting closer. What do you do?")
    print("1. Stay hidden and hope the intruder doesn't find you.")
    print("2. Try to sneak out from under the bed and to the window.")

    hide_under_bed_choice = input(">>>")

    if hide_under_bed_choice == "1":
        stay_hidden()

    elif hide_under_bed_choice == "2":
        sneak_out()

    else:
        print("Invalid choice. Please choose 1, 2, or 3.")
        hide_under_bed()


def call_out_again():
    print("You call out again. The voice responds, 'Come here, please.' What do you do?")
    print("1. Call out, 'Who is this?'")
    print("2. Yell, 'GO AWAY!'")
    print("3. Stay silent.")

    call_out_again_choice = input(">>>")

    if call_out_again_choice == "1":
        call_out_who()

    elif call_out_again_choice == "2":
        yell_go_away()

    elif call_out_again_choice == "3":
        stay_silent()

    else:
        print("Invalid choice. Please choose 1, 2, or 3.")
        call_out_again()


def leave_the_room():
    print("You leave the room. What should you do next?")
    print("1. Check the living room.")
    print("2. Check the kitchen.")
    print("3. Check the closet.")

    leave_the_room_choice = input(">>>")

    if leave_the_room_choice == "1":
        check_living_room()

    elif leave_the_room_choice == "2":
        check_kitchen()

    elif leave_the_room_choice == "3":
        check_closet()

    else:
        print("Invalid choice. Please choose 1, 2, or 3.")
        leave_the_room()


def close_eyes():
    print("You close your eyes and try to go back to sleep. You hear 3 loud bangs at your bedroom door.")
    print("Then, a lanky creature runs at you and eats you.")
    print("GAME OVER.")


def grab_weapon():
    print("You get out of bed and search for a weapon. Which one should you pick?")
    print("1. A baseball bat.")
    print("2. An IPhone Charger.")
    print("3. A Nerf Gun.")

    grab_weapon_choice = input(">>>")

    if grab_weapon_choice == "1":
        grab_baseball_bat()

    elif grab_weapon_choice == "2":
        grab_charger()

    elif grab_weapon_choice == "3":
        grab_nerf_gun()

    else:
        print("Invalid choice. Please choose 1, 2, or 3.")
        grab_weapon()


def call_911():
    print("Your hands shake as you dial 911. The operator answers and you tell them about the voice.")
    print("The operator needs your address. You blank, and forget where you live entirely.")
    print("All the while, the voice's footsteps are getting closer. You drop your phone.")
    print("The intruder finds you and eats you.")
    print("GAME OVER.")


def stay_hidden():
    print("You stay hidden under the bed. You hold your breath.")
    print("You close your eyes, hoping the intruder won't find you.")
    print("You hear the door knob turn...")
    print("The intruder finds you and eats you.")
    print("GAME OVER.")


def sneak_out():
    print("You hear the voice get louder as you scramble for the window.")
    print("You open the window and jump out. What do you do next?")
    print("1. Run to the neighbor's house.")
    print("2. Run to the park.")
    print("3. Run to the police station.")

    sneak_out_choice = input(">>>")

    if sneak_out_choice == "1":
        run_to_neighbor()

    elif sneak_out_choice == "2":
        run_to_park()

    elif sneak_out_choice == "3":
        run_to_police_station()

    else:
        print("Invalid choice. Please choose 1, 2, or 3.")
        sneak_out()


def call_out_who():
    print("You call out, 'Who is this?' The voice calls out again, 'Please, come here.' What do you do?")
    print("1. Ask, 'Where are you?'")
    print("2. Open the bedroom door and exit.")

    call_out_who_choice = input(">>>")

    if call_out_who_choice == "1":
        where_are_you()

    elif call_out_who_choice == "2":
        exit_bedroom()

    else:
        print("Invalid choice. Please choose 1, 2, or 3.")
        call_out_who()

def yell_go_away():
    print("You yell, 'GO AWAY!' Footsteps slowly make their way to your door.")
    print("The door opens and a lanky creature runs at you and eats you.")
    print("GAME OVER.")


def check_living_room():
    print("You check the living room. It's empty. You hear a noise coming from the kitchen.")
    print("What do you do?")
    print("1. Check the kitchen.")
    print("2. Check the closet.")

    check_living_room_choice = input(">>>")

    if check_living_room_choice == "1":
        check_kitchen()

    elif check_living_room_choice == "2":
        check_closet()

    else:
        print("Invalid choice. Please choose 1, 2, or 3.")
        check_living_room()


def check_kitchen():
    print("You check the kitchen. It's empty.")
    print("You look out the window and see a figure standing in your backyard. What do you do?")
    print("1. Lock the door.")
    print("2. Wave at the figure.")
    print("3. Turn out the lights.")

    check_kitchen_choice = input(">>>")

    if check_kitchen_choice == "1":
        lock_door()

    elif check_kitchen_choice == "2":
        wave_at_figure()

    elif check_kitchen_choice == "3":
        turn_out_lights()

    else:
        print("Invalid choice. Please choose 1, 2, or 3.")
        check_kitchen()


def check_closet():
    print("You check the closet. You rifle trough the clothes.")
    print("You hear a whisper come from the back of the closet.")
    print("Two back hands reach out to you and pull you into the closet. The intruder eats you.")    
    print("GAME OVER.")


def grab_baseball_bat():
    print("You grab the baseball bat and wait for the intruder to come into your room.")
    print("The door open and a lanky creature enters.")
    print("You hit the creature in the head with the baseball bat. The creature is stunned and you have a chance to escape.")
    print("What do you do?")
    print("1. Run to the neighbor's house.")
    print("2. Run to the park.")
    print("3. Run to the police station.")

    grab_baseball_bat_choice = input(">>>")

    if grab_baseball_bat_choice == "1":
        run_to_neighbor()

    elif grab_baseball_bat_choice == "2":
        run_to_park()

    elif grab_baseball_bat_choice == "3":
        run_to_police_station()

    else:
        print("Invalid choice. Please choose 1, 2, or 3.")
        grab_baseball_bat()


def grab_charger():
    print("You grab the iPhone charger and wait for the intruder to come into your room.")
    print("The door open and a lanky creature enters.")
    print("You try to hit the creature with the charger, but it doesn't do any damage.")
    print("The creature is not stunned and you have no chance to escape.")
    print("The creature eats you.")
    print("GAME OVER.")


def grab_nerf_gun():
    print("You grab the nerf gun and wait for the intruder to come into your room.")
    print("The door open and a lanky creature enters.")
    print("You try to shoot the creature, but the foam bullet bounces off the creature's skin and does no damage.")
    print("The creature is confused and looks at you like you're an idiot.")
    print("The creature eats you.")
    print("GAME OVER.")


def run_to_neighbor():
    print("You run to your neighbor's house and knock on the door. Your neighbor answers and you tell them about the voice.")
    print("Your neighbor calls the police and they arrive shortly after.")
    print("The police search your house but find no one there. They tell you to stay at your neighbor's house for the night.")
    print("You stay at your neighbor's house and the next day, you find out that the intruder was taken care of.")
    print("CONGRATS! YOU WIN!")


def run_to_park():
    print("You run to the park and hide behind a tree. You see a lanky, scary creature walkings towards you.")
    print("The creature sees you and starts chasing you. You run as fast as you can, but the creature is faster than you.")
    print("The creature catches you and eats you.")
    print("GAME OVER.")


def run_to_police_station():
    print("You run to the police station for help.")
    print("You tell them about the voice frantically, but they don't take you seriously.")
    print("They tell you to go home and lock your doors.")
    print("You go back home and lock your doors, but there is a lanky creature waiting for you.")
    print("The creature eats you.")
    print("GAME OVER.")


def where_are_you():
    print("You ask, 'Where are you?' The voice responds, 'I'm in the kitchen.' What do you do?")
    print("1. Go to the kitchen.")
    print("2. Grab a weapon and go to the kitchen.")

    where_are_you_choice = input(">>>")

    if where_are_you_choice == "1":
        check_kitchen()

    elif where_are_you_choice == "2":
        grab_weapon()

    else:
        print("Invalid choice. Please choose 1, 2, or 3.")
        where_are_you()


def exit_bedroom():
    print("You open the bedroom door and exit. You see a lanky creature standing in your hallway.")
    print("The creature eats you.")
    print("GAME OVER.")


def lock_door():
    print("You lock the door, but the figure appears out of thin air.")
    print("The lanky creature say, 'Hello, " + name + ".' The creature eats you.")
    print("GAME OVER.")


def wave_at_figure():
    print("You wave at the figure. The figure waves back and says, 'Hello, " + name + ".' The figure is actually a friendly neighbor who was trying to check on you.")
    print("The neighbor asks if you were okay, and you tell them about the voice.")
    print("The neighbor says, 'It was probably just a dream.' with a scary smile.")
    print("You still feel uneasy, but you go back to bed and try to sleep. You never hear the voice again.")
    print("CONGRATS! YOU WIN!")


def turn_out_lights():
    print("You turn out the lights and hide.")
    print("Little did you know, the mysterious creature can see in the dark.")
    print("The creature finds you and eats you.")
    print("GAME OVER.")


start_game()
