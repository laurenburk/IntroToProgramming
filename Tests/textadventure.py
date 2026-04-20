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
    print("Yell, 'GO AWAY!'")
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


print(start_game())
