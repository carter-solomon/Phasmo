import random

#                                                        #help#
########################################################################################################################
def emf_help():
    print("\n\033[1;35;40mTo use the emf you need to say scan, this will scan for electronic")
    print("disturbances left by the ghost. All ghosts leave some level of")
    print("electronic disturbance but some ghosts will leave an emf level 5.")
    print("If it leaves a level 5 then that counts as evidence. Keep in mind")
    print("you won't know after one scan you may have to try multiple times")
    print("before it leaves a level 5.")

def freezing_temps_help():
    print("\n\033[1;35;40mTo use the freezing temperatures you need to say measure. This")
    print("will measure the temperatures of your location. All ghosts are at")
    print("least a little cold but some are exceedingly cold causing the")
    print("area they're in to reach temperatures below freezing. Keep in mind")
    print("you won't know after one try, you may have to try multiple times")
    print("before it gets below zero.")

def spirit_box_help():
    print("\n\033[1;35;40mTo use the spirit box you need to say certain phrases into it.")
    print("The spirit box allows your voice to cross over into the spirit")
    print("realm allowing ghosts to hear you, certain types of ghosts can")
    print("even respond to you through the spirit box. Keep in mind you")
    print("only certain phrases will give you a response.")
    print("\n\033[1;34;40m** If you want to be lame you can say phrase list")
    print("to see a list of all the phrases you can use **")

def phrase_list():
    print("\n\033[1;35;40mwhere are you, are you here, are you near, is anyone there, how old are you,")
    print("what do you want, show yourself, give me a sign, talk to me, can you speak, are there any ghosts")
    print("let us know you are here, is there anyone here, scream, can we speak, do you speak french")
    print("are you happy, do you want us to leave, can you make a sound, do you want to hurt us")

def ultraviolet_help():
    print("\n\033[1;35;40mTo use the ultraviolet light you have to say look. Some")
    print("ghost leave behind a mark of sorts when they touch stuff.")
    print("When an ultraviolet light is shined on a spot touched by ")
    print("one of these ghosts you can see the mark they left behind.")
    print("Keep in mind it may take you more then one try to see it.")

def ghost_writing_help():
    print("\n\033[1;35;40mTo use the ghost writing book you have to say place. Some")
    print("ghosts like to share information with us in the form of writing.")
    print("So if you put down a book some types of ghosts will write in")
    print("it. Keep in mind it may take you more then one try to see it.")

def dots_help():
    print("\n\033[1;35;40mTo use dots you have to say watch, this will scatter small lasers all throughout")
    print("the room. Some ghosts are more prominent in the living realm then others.")
    print("Do to this they will occasionally become visible when they walk through")
    print("the dots. Keep in mind it may take you more then one try to see it.")

def ghost_orbs_help():
    print("\n\033[1;35;40mTo use the ghost orbs camera you have to say film, this will take ")
    print("footage of the room. Some ghosts leave behind a sort of mystical ")
    print("emanation that clumps together into orbs.These clumps of mystical ")
    print("energy are called ghost orbs and can be seen using ghost orb ")
    print("cameras. Keep in mind it may take you more then one try to see it.")

#                                                  #is evidence#
########################################################################################################################
def emf():
    emf_active = "true"
    while emf_active == "true":
        emf_action = input("\n\033[1;36;40memf on (scan/s): ")
        if emf_action == "help":
            emf_help()
        elif emf_action == "stop":
            emf_active = "false"
        elif emf_action == "scan" or emf_action == "s":
            emf_random = random.randint(0, 19)
            if 0 <= emf_random < 4:
                print("\033[1;37;40mo\033[1;37;40mo\033[1;37;40mo\033[1;37;40mo\033[1;37;40mo")
            elif 4 <= emf_random < 8:
                print("\033[1;34;40mo\033[1;37;40mo\033[1;37;40mo\033[1;37;40mo\033[1;37;40mo")
            elif 8 <= emf_random < 12:
                print("\033[1;34;40mo\033[1;36;40mo\033[1;37;40mo\033[1;37;40mo\033[1;37;40mo")
            elif 12 <= emf_random < 16:
                print("\033[1;34;40mo\033[1;36;40mo\033[1;32;40mo\033[1;37;40mo\033[1;37;40mo")
            elif 16 <= emf_random < 19:
                print("\033[1;34;40mo\033[1;36;40mo\033[1;32;40mo\033[1;33;40mo\033[1;37;40mo")
            elif emf_random == 19:
                print("\033[1;34;40mo\033[1;36;40mo\033[1;32;40mo\033[1;33;40mo\033[1;31;40mo")

def freezing_temps():
    freezing_temps_active = "true"
    temp = random.randint(8, 14)
    while freezing_temps_active == "true":
        freezing_temps_action = input("\n\033[1;36;40mthermometer on (measure/m): \033[1;39;40m")
        if freezing_temps_action == "help":
            freezing_temps_help()
        elif freezing_temps_action == "stop":
            freezing_temps_active = "false"
        elif freezing_temps_action == "measure" or freezing_temps_action == "m":
            temp_change = random.randint(1,3)
            if temp - temp_change < -5:
                temp += temp_change
            elif temp + temp_change > 14:
                temp -= temp_change
            else:
                temp_negative_positive = random.choice(["negative", "positive"])
                if temp_negative_positive == "negative":
                    temp -= temp_change
                else:
                    temp += temp_change
            if temp == 1 or temp == -1:
                print(temp, "degree celsius")
            else:
                print(temp, "degrees celsius")

def spirit_box(age):
    spirit_box_active = "true"
    while spirit_box_active == "true":
        spirit_box_action = input("\n\033[1;36;40mspirit box on: ")
        if spirit_box_action == "help":
            spirit_box_help()
        elif spirit_box_action == "stop":
            spirit_box_active = "false"
        elif spirit_box_action == "phrase list":
            phrase_list()
        elif spirit_box_action in ["are you near","is anyone there","can you speak","are there any ghosts","can we speak","are you happy","do you want us to leave","do you want to hurt us"]:
            random_spirit_box = random.randint(0,5)
            if random_spirit_box == 0:
                print(random.choice(["Yes", "No"]))
            elif random_spirit_box == 1:
                print("RAAAA RAA")
            elif random_spirit_box == 2:
                print("GRAA RA")
            else:
                print("** No response **")
        elif spirit_box_action == "how old are you":
            random_spirit_box = random.randint(0,5)
            if random_spirit_box == 0:
                print("I'm" , age)
            elif random_spirit_box == 1:
                print("RAAAA RAA")
            elif random_spirit_box == 2:
                print("GRAA RA")
            else:
                print("** No response **")
        elif spirit_box_action in ["where are you","are you near","show yourself"]:
            random_spirit_box = random.randint(0, 5)
            if random_spirit_box == 0:
                print(random.choice(["Behind you","Near","Right here","In front of you","To your right","To your left"]))
            elif random_spirit_box == 1:
                print("RAAAA RAA")
            elif random_spirit_box == 2:
                print("GRAA RA")
            else:
                print("** No response **")
        elif spirit_box_action in ["let us know you are here","is there anyone here","can you make a sound","give me a sign","talk to me"]:
            random_spirit_box = random.randint(0, 5)
            if random_spirit_box == 0:
                print(random.choice(["I'm here","Hello","I can hear you","Can you hear me","DIE!"]))
            elif random_spirit_box == 1:
                print("RAAAA RAA")
            elif random_spirit_box == 2:
                print("GRAA RA")
            else:
                print("** No response **")
        elif spirit_box_action == "scream":
            random_spirit_box = random.randint(0, 5)
            if random_spirit_box == 0:
                print(random.choice(["AAAAAAAAAA!","AAA!!!","GRAAAAAAAAAAAAAA!!!!!!","RAAA RAAA RAAAAA!!!","GRA RA GRAAAA RA GRA"]))
            elif random_spirit_box == 1:
                print("RAAAA RAA")
            elif random_spirit_box == 2:
                print("GRAA RA")
            else:
                print("** No response **")
        elif spirit_box_action == "what do you want":
            random_spirit_box = random.randint(0, 5)
            if random_spirit_box == 0:
                print(random.choice(["To KiLl YoU!!","To be free... save me... please...","To go home","I want to find you","I want to play","Can you play with me!"]))
            elif random_spirit_box == 1:
                print("RAAAA RAA")
            elif random_spirit_box == 2:
                print("GRAA RA")
            else:
                print("** No response **")
        elif spirit_box_action == "do you speak french":
            random_spirit_box = random.randint(0, 5)
            if random_spirit_box == 0:
                print(random.choice(["yes","no","Oui","Non","Je veux te tuer","Sauve-moi s'il te plaît, je veux être libéré","tue-moi","je te trouverai","joue avec moi"]))
            elif random_spirit_box == 1:
                print("RAAAA RAA")
            elif random_spirit_box == 2:
                print("GRAA RA")
            else:
                print("** No response **")
        else:
           print("** No response **")

def ultraviolet(random_ghost):
    ultraviolet_active = "true"
    while ultraviolet_active == "true":
        ultraviolet_action = input("\n\033[1;36;40multraviolet light on (look/l): ")
        if ultraviolet_action == "help":
            ultraviolet_help()
        elif ultraviolet_action == "stop":
            ultraviolet_active = "false"
        elif ultraviolet_action == "look" or ultraviolet_action == "l":
            if random_ghost == "wraith":
                random_ultraviolet = random.randint(1,84)
            else:
                random_ultraviolet = random.randint(0, 103)
            if random_ultraviolet == 0:
                print("\033[1;35;40m                         /\\  __  __")
                print("\033[1;35;40m                         \\/  \\/  \\/  __")
                print("\033[1;35;40m                           _______   \\/  __")
                print("\033[1;35;40m                         /         \\___  \\/")
                print("\033[1;39;40m      ____________   _ \033[1;35;40m |             _| \033[1;39;40m   .  ________________")
                print("\033[1;39;40m  ___/          _/ _ . \033[1;35;40m |        ____/   \033[1;39;40m    _ . \\__           \\_____")
                print("\033[1;39;40m /           __/ . _   \033[1;35;40m  \\______/       \033[1;39;40m         .. \\___             \\")
                print("\033[1;39;40m|           /_  ..     \033[1;35;40m                  \033[1;39;40m         .   _  \\            |")
                print("\033[1;39;40m|          | _ .  .    \033[1;35;40m                  \033[1;39;40m           . . _ |         _/")
                print("\033[1;39;40m \\___       \\_ . -   \033[1;35;40m                  \033[1;39;40m           . .  __/        _/")
                print("\033[1;39;40m     \\___    \\__ .  .\033[1;35;40m                  \033[1;39;40m        .  _ __/      ____/")
                print("\033[1;39;40m         \\______\\_ . _\033[1;35;40m     ______      \033[1;39;40m    .   _  ./________/")
                print("\033[1;35;40m                         /        \\")
                print("\033[1;35;40m                        |          |")
                print("\033[1;35;40m                         \\        /")
                print("\033[1;35;40m                          \\______/")
            elif random_ultraviolet == 1:
                print("\033[1;39;40m __________________")
                print("\033[1;39;40m|                  |")
                print("\033[1;39;40m|     ________     |")
                print("\033[1;39;40m|    |\033[1;35;40m   __   \033[1;39;40m|    |")
                print("\033[1;39;40m|    |\033[1;35;40m /    \\ \033[1;39;40m|    |")
                print("\033[1;39;40m|    |\033[1;35;40m |    | \033[1;39;40m|    |")
                print("\033[1;39;40m|    |_\033[1;35;40m\\____/\033[1;39;40m_|    |")
                print("\033[1;39;40m|    |  \033[1;35;40m____  \033[1;39;40m|    |")
                print("\033[1;39;40m|    | \033[1;35;40m/     \\\033[1;39;40m|    |")
                print("\033[1;39;40m|    |        |    |")
                print("\033[1;39;40m|    |________|    |")
                print("\033[1;39;40m|                  |")
                print("\033[1;39;40m|__________________|")
            elif random_ultraviolet == 2:
                print("\033[1;39;40m ___________________")
                print("\033[1;39;40m|    /    |    \\    |")
                print("\033[1;39;40m|   |     |     |   |")
                print("\033[1;39;40m|  /      |      \\  |")
                print("\033[1;39;40m| |_______|_______| |")
                print("\033[1;39;40m| |       |       | |")
                print("\033[1;39;40m|/ \033[1;35;40mlll\033[1;39;40m    |        \\|")
                print("\033[1;39;40m| \033[1;35;40m-|_|\033[1;39;40m    |         |")
                print("\033[1;39;40m|_________|_________|")
            elif random_ultraviolet == 3:
                print("\033[1;39;40m ____________")
                print("\033[1;39;40m|   ______   |")
                print("\033[1;39;40m|   ______   |")
                print("\033[1;39;40m||           |")
                print("\033[1;39;40m|     \033[1;35;40mlll\033[1;39;40m    |")
                print("\033[1;39;40m|    \033[1;35;40m-|_|\033[1;39;40m    |")
                print("\033[1;39;40m|        |@| |")
                print("\033[1;39;40m|            |")
                print("\033[1;39;40m|            |")
                print("\033[1;39;40m|            |")
                print("\033[1;39;40m||           |")
                print("\033[1;39;40m|   ______   |")
                print("\033[1;39;40m|____________|")
            elif random_ultraviolet == 4:
                print("\033[1;39;40m __________________")
                print("\033[1;39;40m|   ____    ____   |")
                print("\033[1;39;40m|  |    |  |    |  |")
                print("\033[1;39;40m|  |    |  |    |  |")
                print("\033[1;39;40m|  |    |  |    |  |")
                print("\033[1;39;40m|  |____|  |____|  |")
                print("\033[1;39;40m|       \033[1;35;40mlll\033[1;39;40m     @  |")
                print("\033[1;39;40m|   ____\033[1;35;40m|_|-\033[1;39;40m____   |")
                print("\033[1;39;40m|  |    |  |    |  |")
                print("\033[1;39;40m|  |    |  |    |  |")
                print("\033[1;39;40m|  |    |  |    |  |")
                print("\033[1;39;40m|  |____|  |____|  |")
                print("\033[1;39;40m|__________________|")
            elif random_ultraviolet == 5:
                print("\033[1;39;40m __________________")
                print("\033[1;39;40m|                  |")
                print("\033[1;39;40m|     ________     |")
                print("\033[1;39;40m|    |        |    |")
                print("\033[1;39;40m|    |        |    |")
                print("\033[1;39;40m|    |        |    |")
                print("\033[1;39;40m|    |________|    |")
                print("\033[1;39;40m|    |\033[1;35;40m  /   \\ \033[1;39;40m|    |")
                print("\033[1;39;40m|    |\033[1;35;40m |    | \033[1;39;40m|    |")
                print("\033[1;39;40m|    |_\033[1;35;40m|___/\033[1;39;40m__|    |")
                print("\033[1;39;40m|     \033[1;35;40m/    |\033[1;39;40m       |")
                print("\033[1;39;40m|_____\033[1;35;40m|____|\033[1;39;40m_______|")
            elif random_ultraviolet == 6:
                print("\033[1;39;40m ___________________")
                print("\033[1;39;40m|    /    |    \\    |")
                print("\033[1;39;40m|   |     |     |   |")
                print("\033[1;39;40m|  /      |      \\  |")
                print("\033[1;39;40m| |_______|_______| |")
                print("\033[1;39;40m| |       |  \033[1;35;40mlll\033[1;39;40m  | |")
                print("\033[1;39;40m|/        |  \033[1;35;40m|_|-\033[1;39;40m  \\|")
                print("\033[1;39;40m|         |         |")
                print("\033[1;39;40m|_________|_________|")
            elif random_ultraviolet == 7:
                print("\033[1;39;40m __________________")
                print("\033[1;39;40m|   ____    ____   |")
                print("\033[1;39;40m|  |    |  |    |  |")
                print("\033[1;39;40m|  |    |  |    |  |")
                print("\033[1;39;40m|  |    |  |    |  |")
                print("\033[1;39;40m|  |____|  |____|  |")
                print("\033[1;39;40m|               @  |")
                print("\033[1;39;40m|   ____    ____   |")
                print("\033[1;39;40m|  |    |  |    |  |")
                print("\033[1;39;40m|  |    |  | \033[1;35;40mlll\033[1;39;40m|  |")
                print("\033[1;39;40m|  |    |  |\033[1;35;40m-|_|\033[1;39;40m|  |")
                print("\033[1;39;40m|  |____|  |____|  |")
                print("\033[1;39;40m|__________________|")
            elif random_ultraviolet == 8:
                print("\033[1;39;40m ____________")
                print("\033[1;39;40m|   ______   |")
                print("\033[1;39;40m|   ______   |")
                print("\033[1;39;40m||           |")
                print("\033[1;39;40m|            |")
                print("\033[1;39;40m|            |")
                print("\033[1;39;40m|        |@| |")
                print("\033[1;39;40m|            |")
                print("\033[1;39;40m|   \033[1;35;40mlll\033[1;39;40m      |")
                print("\033[1;39;40m|   \033[1;35;40m|_|-\033[1;39;40m     |")
                print("\033[1;39;40m||           |")
                print("\033[1;39;40m|   ______   |")
                print("\033[1;39;40m|____________|")
            elif 8 < random_ultraviolet <= 27:
                print("\033[1;39;40m __________________")
                print("\033[1;39;40m|   ____    ____   |")
                print("\033[1;39;40m|  |    |  |    |  |")
                print("\033[1;39;40m|  |    |  |    |  |")
                print("\033[1;39;40m|  |    |  |    |  |")
                print("\033[1;39;40m|  |____|  |____|  |")
                print("\033[1;39;40m|               @  |")
                print("\033[1;39;40m|   ____    ____   |")
                print("\033[1;39;40m|  |    |  |    |  |")
                print("\033[1;39;40m|  |    |  |    |  |")
                print("\033[1;39;40m|  |    |  |    |  |")
                print("\033[1;39;40m|  |____|  |____|  |")
                print("\033[1;39;40m|__________________|")
            elif 27 < random_ultraviolet <= 46:
                print("\033[1;39;40m __________________")
                print("\033[1;39;40m|                  |")
                print("\033[1;39;40m|     ________     |")
                print("\033[1;39;40m|    |        |    |")
                print("\033[1;39;40m|    |        |    |")
                print("\033[1;39;40m|    |        |    |")
                print("\033[1;39;40m|    |________|    |")
                print("\033[1;39;40m|    |        |    |")
                print("\033[1;39;40m|    |        |    |")
                print("\033[1;39;40m|    |        |    |")
                print("\033[1;39;40m|    |________|    |")
                print("\033[1;39;40m|                  |")
                print("\033[1;39;40m|__________________|")
            elif 46 < random_ultraviolet <= 65:
                print("\033[1;39;40m ___________________")
                print("\033[1;39;40m|    /    |    \\    |")
                print("\033[1;39;40m|   |     |     |   |")
                print("\033[1;39;40m|  /      |      \\  |")
                print("\033[1;39;40m| |_______|_______| |")
                print("\033[1;39;40m| |       |       | |")
                print("\033[1;39;40m|/        |        \\|")
                print("\033[1;39;40m|         |         |")
                print("\033[1;39;40m|_________|_________|")
            elif 65 < random_ultraviolet <= 84:
                print("\033[1;39;40m ____________")
                print("\033[1;39;40m|   ______   |")
                print("\033[1;39;40m|   ______   |")
                print("\033[1;39;40m||           |")
                print("\033[1;39;40m|            |")
                print("\033[1;39;40m|            |")
                print("\033[1;39;40m|        |@| |")
                print("\033[1;39;40m|            |")
                print("\033[1;39;40m|            |")
                print("\033[1;39;40m|            |")
                print("\033[1;39;40m|            |")
                print("\033[1;39;40m|   ______   |")
                print("\033[1;39;40m|____________|")
            elif 84 < random_ultraviolet <= 103:
                print("\033[1;39;40m      ____________   _                      .  ________________")
                print("\033[1;39;40m  ___/          _/ _ .                       _ . \\__           \\_____")
                print("\033[1;39;40m /           __/ . _                             .. \\___             \\")
                print("\033[1;39;40m|           /_  ..                                .   _  \\            |")
                print("\033[1;39;40m|          | _ .  .                                 . . _ |         _/")
                print("\033[1;39;40m \\___       \\_ . -                                . .  __/        _/")
                print("\033[1;39;40m     \\___    \\__ .  .                          .  _ __/      ____/")
                print("\033[1;39;40m         \\______\\_ . _                     .   _  ./________/")

def ghost_writing():
    ghost_writing_active = "true"
    while ghost_writing_active == "true":
        ghost_writing_action = input("\n\033[1;36;40mbook in hand (place/p): ")
        if ghost_writing_action == "help":
            ghost_writing_help()
        elif ghost_writing_action == "stop":
            ghost_writing_active = "false"
        elif ghost_writing_action == "place" or ghost_writing_action == "p":
            ghost_writing_random = random.randint(0,130)
            if ghost_writing_random == 0:
                print("\033[1;35;40m _______________/---\\_______________")
                print("\033[1;39;40m|  . .  _ .   _   |  _   _   _   _  |")
                print("\033[1;39;40m|  |_| |_ |  |_|  | |_| |_| |_| |_| |")
                print("\033[1;39;40m|  | | |_ |_ |    | | | | | | | | | |")
                print("\033[1;39;40m|  .  .   _       |  _   _   _   _  |")
                print("\033[1;39;40m|  |\\/|  |_       | |_| |_| |_| |_| |")
                print("\033[1;39;40m|  |  |  |_       | | | | | | | | | |")
                print("\033[1;39;40m|\033[1;35;40m________________/ \\________________\033[1;39;40m|")
            elif ghost_writing_random == 1:
                print("\033[1;35;40m _______________/---\\_______________")
                print("\033[1;39;40m|  _   _ . .      | . .  _   . .    |")
                print("\033[1;39;40m| |_/ |_ |_|      |  V  | |  | |    |")
                print("\033[1;39;40m| |_\\ |_ | |      |  |  |_|  |_|    |")
                print("\033[1;39;40m|  ___ .  .  __   |    ___   ___    |")
                print("\033[1;39;40m|   |  |\\ | |  \\  |   | O | | O |   |")
                print("\033[1;39;40m|  _|_ | \\| |__/  |    ---   ---    |")
                print("\033[1;39;40m|\033[1;35;40m________________/ \\________________\033[1;39;40m|")
            elif ghost_writing_random == 2:
                print("\033[1;35;40m _______________/---\\_______________")
                print("\033[1;39;40m|  \\ /|\\ /|\\ /    |   \\ /  |  / \\   |")
                print("\033[1;39;40m|  /_\\|/_\\|/_\\    |  _/_\\__|__\\_/_  |")
                print("\033[1;39;40m|     |/ \\|       |        |        |")
                print("\033[1;39;40m|  ___|\\_/|___    |   |||| | ||     |")
                print("\033[1;39;40m|  / \\|\\ /|/ \\    |        |        |")
                print("\033[1;39;40m|  \\ /|/ \\|\\ /    |        |        |")
                print("\033[1;39;40m|\033[1;35;40m________________/ \\________________\033[1;39;40m|")
            elif ghost_writing_random == 3:
                print("\033[1;35;40m _______________/---\\_______________")
                print("\033[1;39;40m|      __|__      |                 |")
                print("\033[1;39;40m|     /  |  \\     | |   _           |")
                print("\033[1;39;40m|  --|---+---|--  | | _/ \\_         |")
                print("\033[1;39;40m|     \\__|__/     | |/_____\\_______/|")
                print("\033[1;39;40m|        |        | |       \\_   _/ |")
                print("\033[1;39;40m|                 | |         \\_/   |")
                print("\033[1;39;40m|\033[1;35;40m________________/ \\________________\033[1;39;40m|")
            elif ghost_writing_random == 4:
                print("\033[1;35;40m _______________/---\\_______________")
                print("\033[1;39;40m|    ___          | |  |  _         |")
                print("\033[1;39;40m| |/  |  |  |     | |/\\| |_| ___    |")
                print("\033[1;39;40m| |\\ _|_ |_ |_    |      | |  | ___ |")
                print("\033[1;39;40m| .  .  _         | |\\ |  _  _|_ |  |")
                print("\033[1;39;40m| |\\/| |_         | | \\| | |     |  |")
                print("\033[1;39;40m| |  | |_ o o o   |      |_|        |")
                print("\033[1;39;40m|\033[1;35;40m________________/ \\________________\033[1;39;40m|")
            elif ghost_writing_random == 5:
                print("\033[1;35;40m _______________/---\\_______________")
                print("\033[1;39;40m|       ___       |    ___ .   .    |")
                print("\033[1;39;40m|        |        | |/  |  |   |    |")
                print("\033[1;39;40m|       _|_       | |\\ _|_ |__ |__  |")
                print("\033[1;39;40m| . . . .  _  ___ |  .  .  _        |")
                print("\033[1;39;40m| |_| | | |_|  |  |  |\\/| |_        |")
                print("\033[1;39;40m| | | |_| |\\   |  |  |  | |_        |")
                print("\033[1;39;40m|\033[1;35;40m________________/ \\________________\033[1;39;40m|")
            elif ghost_writing_random == 6:
                print("\033[1;35;40m _______________/---\\_______________")
                print("\033[1;39;40m|                 |                 |")
                print("\033[1;39;40m| _|_|_|_|        |   _|_|_         |")
                print("\033[1;39;40m| _|_|_|_|_|_     | _|_|_|_|_|_     |")
                print("\033[1;39;40m| _|_|_|_|_|_|_   | _|_|_|_|_|_|_   |")
                print("\033[1;39;40m|  | |_|_|_| |    | _|_|_|_| | |    |")
                print("\033[1;39;40m|    | | | |      |  | | | |        |")
                print("\033[1;39;40m|\033[1;35;40m________________/ \\________________\033[1;39;40m|")
            elif ghost_writing_random == 7:
                print("\033[1;35;40m _______________/---\\_______________")
                print("\033[1;39;40m|  ___            |                 |")
                print("\033[1;39;40m| /0 0\\           | 0      0        |")
                print("\033[1;39;40m| \\___/           | T      T        |")
                print("\033[1;39;40m| __|__           | ^      ^        |")
                print("\033[1;39;40m|   |             |                 |")
                print("\033[1;39;40m|  /\\             |                 |")
                print("\033[1;39;40m|\033[1;35;40m________________/ \\________________\033[1;39;40m|")
            elif ghost_writing_random == 8:
                print("\033[1;35;40m _______________/---\\_______________")
                print("\033[1;39;40m|        /   ___  |                 |")
                print("\033[1;39;40m|   __-_|   /     |   __      _-__  |")
                print("\033[1;39;40m|  |    /\\  \\  __ |     \\  \\ /  _ \\ |")
                print("\033[1;39;40m|   \\__/  |   |/  |    _/   |    \\| |")
                print("\033[1;39;40m|    \\    \\__/\\   |   /     /  __/| |")
                print("\033[1;39;40m|    /       |    |   \\____/     /  |")
                print("\033[1;39;40m|\033[1;35;40m________________/ \\________________\033[1;39;40m|")
            elif 9 < ghost_writing_random <= 130:
                print("\033[1;35;40m _______________/---\\_______________")
                print("\033[1;39;40m|                 |                 |")
                print("\033[1;39;40m|                 |                 |")
                print("\033[1;39;40m|                 |                 |")
                print("\033[1;39;40m|                 |                 |")
                print("\033[1;39;40m|                 |                 |")
                print("\033[1;39;40m|                 |                 |")
                print("\033[1;39;40m|\033[1;35;40m________________/ \\________________\033[1;39;40m|")

def dots(room):
    dots_active = "true"
    while dots_active == "true":
        dots_action = input("\n\033[1;36;40mdots on (watch/w): ")
        if dots_action == "help":
            dots_help()
        elif dots_action == "stop":
            dots_active = "false"
        elif dots_action == "watch" or dots_action == "w":
            dots_random = random.randint(0,40)
            if room == 0:
                if dots_random == 0:
                    print("\033[1;37;40m|---------------------------------------|")
                    print("\033[1;37;40m| \033[1;32;40m.  .  .  .  .  .  .  .  .  . \033[1;37;40m|        |")
                    print("\033[1;37;40m| \033[1;32;40m.  .  .  .  .  .  .  .  .  . \033[1;37;40m|        |")
                    print("\033[1;37;40m| \033[1;32;40m.  .  .  .  .  .  .  .O .  . \033[1;37;40m|____    |")
                    print("\033[1;37;40m| \033[1;32;40m.  .  .  .  .  .  .  ooo.  .  .  .\033[1;37;40m|   |")
                    print("\033[1;37;40m| \033[1;32;40m.  .  .  .  .  .  . o o o  .  \033[1;37;40m___ |   |")
                    print("\033[1;37;40m| _____________  \033[1;32;40m. \033[1;37;40m|\033[1;32;40m.   o .  .\033[1;37;40m__|_|_|   |")
                    print("\033[1;37;40m|  | \033[1;32;40m.  .  . \033[1;37;40m|  ___|\033[1;32;40m.  o o.  .\033[1;37;40m|         |")
                    print("\033[1;37;40m|  | \033[1;32;40m.  .  . \033[1;37;40m|  |  |\033[1;32;40m.  o o.  .\033[1;37;40m|         |")
                    print("\033[1;37;40m|---------------------------------------|")
                elif dots_random == 1:
                    print("\033[1;37;40m|---------------------------------------|")
                    print("\033[1;37;40m| \033[1;32;40m.  .  .  .  .  .  .  .  .  . \033[1;37;40m|        |")
                    print("\033[1;37;40m| \033[1;32;40m.  .  .  .  .  .  .  .  .  . \033[1;37;40m|        |")
                    print("\033[1;37;40m| \033[1;32;40m.  .  O  .  .  .  .  .  .  . \033[1;37;40m|____    |")
                    print("\033[1;37;40m| \033[1;32;40m.  . ooo .  .  .  .  .  .  .  .  .\033[1;37;40m|   |")
                    print("\033[1;37;40m| \033[1;32;40m.  .o o o.  .  .  .  .  .  .  \033[1;37;40m___ |   |")
                    print("\033[1;37;40m| ______\033[1;32;40mo\033[1;37;40m______  \033[1;32;40m. \033[1;37;40m|\033[1;32;40m.  .  .  .\033[1;37;40m__|_|_|   \033[1;37;40m|")
                    print("\033[1;37;40m|  | \033[1;32;40m. o o . \033[1;37;40m|  ___|\033[1;32;40m.  .  .  .\033[1;37;40m|         |")
                    print("\033[1;37;40m|  | \033[1;32;40m. o o . \033[1;37;40m|  |  |\033[1;32;40m.  .  .  .\033[1;37;40m|         |")
                    print("\033[1;37;40m|---------------------------------------|")
                elif dots_random == 2:
                    print("\033[1;37;40m|---------------------------------------|")
                    print("\033[1;37;40m| \033[1;32;40m.  .  .  .  .  .  .  .  .  . \033[1;37;40m|        |")
                    print("\033[1;37;40m| \033[1;32;40m.  .  .  .  .  .  .  .  .  . \033[1;37;40m|        |")
                    print("\033[1;37;40m| \033[1;32;40m.  .  .  .  .  .  .  .  .  . \033[1;37;40m|____    |")
                    print("\033[1;37;40m| \033[1;32;40m.  .  .  .  .  .  .  .  .  .  .  .\033[1;37;40m|   |")
                    print("\033[1;37;40m| \033[1;32;40m.  .  .  .  .  .  .  .  .  .  \033[1;37;40m___ |   |")
                    print("\033[1;37;40m| _____________  \033[1;32;40m. \033[1;37;40m|\033[1;32;40m.  .  .  .\033[1;37;40m__|_|_|   |")
                    print("\033[1;37;40m|  | \033[1;32;40m.  .  . \033[1;37;40m|  ___|\033[1;32;40m.  oooo.O \033[1;37;40m|         |")
                    print("\033[1;37;40m|  | \033[1;32;40m.  .  . \033[1;37;40m|  |  | \033[1;32;40mooO  O   \033[1;37;40m|         |")
                    print("\033[1;37;40m|---------------------------------------|")
                elif dots_random == 3:
                    print("\033[1;37;40m|---------------------------------------|")
                    print("\033[1;37;40m| \033[1;32;40m.  .  .  .  .  .  .  .  .  . \033[1;37;40m|        |")
                    print("\033[1;37;40m| \033[1;32;40m.  .  .  .  .  .  .  .  .  . \033[1;37;40m|        |")
                    print("\033[1;37;40m| \033[1;32;40m.  .  .  .  .  .O .  .  .  . \033[1;37;40m|____    |")
                    print("\033[1;37;40m| \033[1;32;40m.  .  .  .  .  ooo.  .  .  .  .  .\033[1;37;40m|   |")
                    print("\033[1;37;40m| \033[1;32;40m.  .  .  .   o o  o  .  .  .  \033[1;37;40m___ |   |")
                    print("\033[1;37;40m| _____________  \033[1;32;40mo \033[1;37;40m|\033[1;32;40m.  .  .  .\033[1;37;40m__|_|_|   |")
                    print("\033[1;37;40m|  | \033[1;32;40m.  .  . \033[1;37;40m| \033[1;32;40mo\033[1;37;40m_\033[1;32;40mo\033[1;37;40m_|\033[1;32;40m.  .  .  .\033[1;37;40m|         |")
                    print("\033[1;37;40m|  | \033[1;32;40m.  .  . \033[1;37;40m| \033[1;32;40mo\033[1;37;40m| \033[1;32;40mo\033[1;37;40m|\033[1;32;40m.  .  .  .\033[1;37;40m|         |")
                    print("\033[1;37;40m|---------------------------------------|")
                elif 3 < dots_random <= 40:
                    print("\033[1;37;40m|---------------------------------------|")
                    print("\033[1;37;40m| \033[1;32;40m.  .  .  .  .  .  .  .  .  . \033[1;37;40m|        |")
                    print("\033[1;37;40m| \033[1;32;40m.  .  .  .  .  .  .  .  .  . \033[1;37;40m|        |")
                    print("\033[1;37;40m| \033[1;32;40m.  .  .  .  .  .  .  .  .  . \033[1;37;40m|____    |")
                    print("\033[1;37;40m| \033[1;32;40m.  .  .  .  .  .  .  .  .  .  .  .\033[1;37;40m|   |")
                    print("\033[1;37;40m| \033[1;32;40m.  .  .  .  .  .  .  .  .  .  \033[1;37;40m___ |   |")
                    print("\033[1;37;40m| _____________  \033[1;32;40m. \033[1;37;40m|\033[1;32;40m.  .  .  .\033[1;37;40m__|_|_|   |")
                    print("\033[1;37;40m|  | \033[1;32;40m.  .  . \033[1;37;40m|  ___|\033[1;32;40m.  .  .  .\033[1;37;40m|         |")
                    print("\033[1;37;40m|  | \033[1;32;40m.  .  . \033[1;37;40m|  |  |\033[1;32;40m.  .  .  .\033[1;37;40m|         |")
                    print("\033[1;37;40m|---------------------------------------|")
            elif room == 1:
                if dots_random == 0:
                    print("\033[1;37;40m|---------------------------------------|")
                    print("\033[1;37;40m| \033[1;32;40m.  .  .  .  .  .  .  .  .  .  .  .  . \033[1;37;40m|")
                    print("\033[1;37;40m| \033[1;32;40m.  .  .  .  .  .  .  .  .  \033[1;37;40m_________\033[1;32;40m. \033[1;37;40m|")
                    print("\033[1;37;40m| \033[1;32;40m. \033[1;37;40m_________ \033[1;32;40m.  O  .  .  .  \033[1;37;40m|  \033[1;32;40m.  . \033[1;37;40m|\033[1;32;40m. \033[1;37;40m|")
                    print("\033[1;37;40m| \033[1;32;40m. \033[1;37;40m|\033[1;32;40m.  .  .\033[1;37;40m| \033[1;32;40m. ooo .  .  .  \033[1;37;40m|_______|\033[1;32;40m. \033[1;37;40m|")
                    print("\033[1;37;40m| \033[1;32;40m. \033[1;37;40m|_______| \033[1;32;40m.o o o.\033[1;37;40m________|  \033[1;32;40m.  . \033[1;37;40m|\033[1;32;40m. \033[1;37;40m|")
                    print("\033[1;37;40m| \033[1;32;40m. \033[1;37;40m|\033[1;32;40m.  .  .\033[1;37;40m| \033[1;32;40m.  o  .\033[1;37;40m| \033[1;32;40m.  .  \033[1;37;40m|_______|\033[1;32;40m. \033[1;37;40m|")
                    print("\033[1;37;40m| \033[1;32;40m. \033[1;37;40m|_______| \033[1;32;40m. o o .\033[1;37;40m|_______|  \033[1;32;40m.  . \033[1;37;40m|\033[1;32;40m. \033[1;37;40m|")
                    print("\033[1;37;40m| \033[1;32;40m. \033[1;37;40m|\033[1;32;40m.  .  .\033[1;37;40m| \033[1;32;40m. o o .\033[1;37;40m| \033[1;32;40m.  .  \033[1;37;40m|_______|\033[1;32;40m. \033[1;37;40m|")
                    print("\033[1;37;40m|---------------------------------------|")
                elif dots_random == 1:
                    print("\033[1;37;40m|---------------------------------------|")
                    print("\033[1;37;40m| \033[1;32;40m.  .  .  .  .  .  .  .  .  .  .  .  . \033[1;37;40m|")
                    print("\033[1;37;40m| \033[1;32;40m.  .  .  .  .  .  .  .  .  \033[1;37;40m_________\033[1;32;40m. \033[1;37;40m|")
                    print("\033[1;37;40m| \033[1;32;40m. \033[1;37;40m_________ \033[1;32;40m.  .  .  .  .  \033[1;37;40m|  \033[1;32;40m. O. \033[1;37;40m|\033[1;32;40m. \033[1;37;40m|")
                    print("\033[1;37;40m| \033[1;32;40m. \033[1;37;40m|\033[1;32;40m.  .  .\033[1;37;40m| \033[1;32;40m.  .  .  .  .  \033[1;37;40m|___\033[1;32;40mooo\033[1;37;40m_|\033[1;32;40m. \033[1;37;40m|")
                    print("\033[1;37;40m| \033[1;32;40m. \033[1;37;40m|_______| \033[1;32;40m.  .  .\033[1;37;40m________|  \033[1;32;40mo o o\033[1;37;40m|\033[1;32;40m. \033[1;37;40m|")
                    print("\033[1;37;40m| \033[1;32;40m. \033[1;37;40m|\033[1;32;40m.  .  .\033[1;37;40m| \033[1;32;40m.  .  .\033[1;37;40m| \033[1;32;40m.  .  \033[1;37;40m|____\033[1;32;40mo\033[1;37;40m__|\033[1;32;40m. \033[1;37;40m|")
                    print("\033[1;37;40m| \033[1;32;40m. \033[1;37;40m|_______| \033[1;32;40m.  .  .\033[1;37;40m|_______|  \033[1;32;40m.o o \033[1;37;40m|\033[1;32;40m. \033[1;37;40m|")
                    print("\033[1;37;40m| \033[1;32;40m. \033[1;37;40m|\033[1;32;40m.  .  .\033[1;37;40m| \033[1;32;40m.  .  .\033[1;37;40m| \033[1;32;40m.  .  \033[1;37;40m|___\033[1;32;40mo\033[1;37;40m_\033[1;32;40mo\033[1;37;40m_|\033[1;32;40m. \033[1;37;40m|")
                    print("\033[1;37;40m|---------------------------------------|")
                elif dots_random == 2:
                    print("\033[1;37;40m|---------------------------------------|")
                    print("\033[1;37;40m| \033[1;32;40m.  .  .  .  .  .  .  .  .  .  .  .  . \033[1;37;40m|")
                    print("\033[1;37;40m| \033[1;32;40m.  .  .  .  .  .  .  .  .  \033[1;37;40m_________\033[1;32;40m. \033[1;37;40m|")
                    print("\033[1;37;40m| \033[1;32;40m. \033[1;37;40m_________ \033[1;32;40m.  .  .  .  .  \033[1;37;40m|  \033[1;32;40m.  . \033[1;37;40m|\033[1;32;40m. \033[1;37;40m|")
                    print("\033[1;37;40m| \033[1;32;40m. \033[1;37;40m|\033[1;32;40m.  .  .\033[1;37;40m| \033[1;32;40m.  .  .  .  .  \033[1;37;40m|_______|\033[1;32;40m. \033[1;37;40m|")
                    print("\033[1;37;40m| \033[1;32;40m. \033[1;37;40m|_______| \033[1;32;40m.  .  .\033[1;37;40m________|  \033[1;32;40m.  . \033[1;37;40m|\033[1;32;40m. \033[1;37;40m|")
                    print("\033[1;37;40m| \033[1;32;40m. \033[1;37;40m|\033[1;32;40m.  .  .\033[1;37;40m| \033[1;32;40m.  .  .\033[1;37;40m| \033[1;32;40m.  .  \033[1;37;40m|_______|\033[1;32;40m. \033[1;37;40m|")
                    print("\033[1;37;40m| \033[1;32;40m. \033[1;37;40m|_______| \033[1;32;40m.O.oooo\033[1;37;40m|_______|  \033[1;32;40m.  . \033[1;37;40m|\033[1;32;40m. \033[1;37;40m|")
                    print("\033[1;37;40m| \033[1;32;40m. \033[1;37;40m|\033[1;32;40m.  .  .\033[1;37;40m| \033[1;32;40m.  O  O\033[1;37;40m|\033[1;32;40mo.  .  \033[1;37;40m|_______|\033[1;32;40m. \033[1;37;40m|")
                    print("\033[1;37;40m|---------------------------------------|")
                elif dots_random == 3:
                    print("\033[1;37;40m|---------------------------------------|")
                    print("\033[1;37;40m| \033[1;32;40m.  .  .  .  .  .  .  .  .  .  .  .  . \033[1;37;40m|")
                    print("\033[1;37;40m| \033[1;32;40m.  .  .  .  .  .  .  .  .  \033[1;37;40m_________\033[1;32;40m. \033[1;37;40m|")
                    print("\033[1;37;40m| \033[1;32;40m. \033[1;37;40m___\033[1;32;40mO\033[1;37;40m_____ \033[1;32;40m.  .  .  .  .  \033[1;37;40m|  \033[1;32;40m.  . \033[1;37;40m|\033[1;32;40m. \033[1;37;40m|")
                    print("\033[1;37;40m| \033[1;32;40m. \033[1;37;40m|\033[1;32;40m.ooo  .\033[1;37;40m| \033[1;32;40m.  .  .  .  .  \033[1;37;40m|_______|\033[1;32;40m. \033[1;37;40m|")
                    print("\033[1;37;40m| \033[1;32;40m. \033[1;37;40m|_\033[1;32;40mo\033[1;37;40m_\033[1;32;40mo\033[1;37;40m_\033[1;32;40mo\033[1;37;40m_| \033[1;32;40m.  .  .\033[1;37;40m________|  \033[1;32;40m.  . \033[1;37;40m|\033[1;32;40m. \033[1;37;40m|")
                    print("\033[1;37;40m| \033[1;32;40m. \033[1;37;40m|\033[1;32;40m.  o  .\033[1;37;40m| \033[1;32;40m.  .  .\033[1;37;40m| \033[1;32;40m.  .  \033[1;37;40m|_______|\033[1;32;40m. \033[1;37;40m|")
                    print("\033[1;37;40m| \033[1;32;40m. \033[1;37;40m|__\033[1;32;40mo\033[1;37;40m_\033[1;32;40mo\033[1;37;40m__| \033[1;32;40m.  .  .\033[1;37;40m|_______|  \033[1;32;40m.  . \033[1;37;40m|\033[1;32;40m. \033[1;37;40m|")
                    print("\033[1;37;40m| \033[1;32;40m. \033[1;37;40m|\033[1;32;40m.o  o .\033[1;37;40m| \033[1;32;40m.  .  .\033[1;37;40m| \033[1;32;40m.  .  \033[1;37;40m|_______|\033[1;32;40m. \033[1;37;40m|")
                    print("\033[1;37;40m|---------------------------------------|")
                elif 3 < dots_random <= 40:
                    print("\033[1;37;40m|---------------------------------------|")
                    print("\033[1;37;40m| \033[1;32;40m.  .  .  .  .  .  .  .  .  .  .  .  . \033[1;37;40m|")
                    print("\033[1;37;40m| \033[1;32;40m.  .  .  .  .  .  .  .  .  \033[1;37;40m_________\033[1;32;40m. \033[1;37;40m|")
                    print("\033[1;37;40m| \033[1;32;40m. \033[1;37;40m_________ \033[1;32;40m.  .  .  .  .  \033[1;37;40m|  \033[1;32;40m.  . \033[1;37;40m|\033[1;32;40m. \033[1;37;40m|")
                    print("\033[1;37;40m| \033[1;32;40m. \033[1;37;40m|\033[1;32;40m.  .  .\033[1;37;40m| \033[1;32;40m.  .  .  .  .  \033[1;37;40m|_______|\033[1;32;40m. \033[1;37;40m|")
                    print("\033[1;37;40m| \033[1;32;40m. \033[1;37;40m|_______| \033[1;32;40m.  .  .\033[1;37;40m________|  \033[1;32;40m.  . \033[1;37;40m|\033[1;32;40m. \033[1;37;40m|")
                    print("\033[1;37;40m| \033[1;32;40m. \033[1;37;40m|\033[1;32;40m.  .  .\033[1;37;40m| \033[1;32;40m.  .  .\033[1;37;40m| \033[1;32;40m.  .  \033[1;37;40m|_______|\033[1;32;40m. \033[1;37;40m|")
                    print("\033[1;37;40m| \033[1;32;40m. \033[1;37;40m|_______| \033[1;32;40m.  .  .\033[1;37;40m|_______|  \033[1;32;40m.  . \033[1;37;40m|\033[1;32;40m. \033[1;37;40m|")
                    print("\033[1;37;40m| \033[1;32;40m. \033[1;37;40m|\033[1;32;40m.  .  .\033[1;37;40m| \033[1;32;40m.  .  .\033[1;37;40m| \033[1;32;40m.  .  \033[1;37;40m|_______|\033[1;32;40m. \033[1;37;40m|")
                    print("\033[1;37;40m|---------------------------------------|")
            elif room == 2:
                if dots_random == 0:
                    print("\033[1;37;40m|---------------------------------------|")
                    print("\033[1;37;40m| \033[1;32;40m.  .  .  .  .  .  .  .  .  .  .  .  . \033[1;37;40m|")
                    print("\033[1;37;40m| \033[1;32;40m.  .  .  .  .  .  .  .  .  .  .  .  . \033[1;37;40m|")
                    print("\033[1;37;40m| \033[1;32;40m.  .  .  .O .  .  .  .  .  .  .  .  . \033[1;37;40m|")
                    print("\033[1;37;40m| __ \033[1;32;40m.  .  ooo.  .  .  .  .  \033[1;37;40m|  \033[1;32;40m.  .\033[1;37;40m| \033[1;32;40m. \033[1;37;40m|")
                    print("\033[1;37;40m| || \033[1;32;40m.  . o o o  . \033[1;37;40m__  \033[1;32;40m.  .  \033[1;37;40m| __===|_| |")
                    print("\033[1;37;40m| ||________\033[1;32;40mo\033[1;37;40m______||  .  .  \033[1;37;40m|_|      | |")
                    print("\033[1;37;40m| ||_______________||  \033[1;32;40m.  .  \033[1;37;40m| |______| |")
                    print("\033[1;37;40m| || \033[1;32;40m.  .  .  .  . \033[1;37;40m||  \033[1;32;40m.  .  \033[1;37;40m| |  |   | |")
                    print("\033[1;37;40m|---------------------------------------|")
                elif dots_random == 1:
                    print("\033[1;37;40m|---------------------------------------|")
                    print("\033[1;37;40m| \033[1;32;40m.  .  .  .  .  .  .  .  .  .  .  .  . \033[1;37;40m|")
                    print("\033[1;37;40m| \033[1;32;40m.  .  .  .  .  .  .  .  .  .  .  .  . \033[1;37;40m|")
                    print("\033[1;37;40m| \033[1;32;40m.  .  .  .  .  .  .  .  .  .  .  .  . \033[1;37;40m|")
                    print("\033[1;37;40m| __ \033[1;32;40m.  .  .  .  .  .  .  .  \033[1;37;40m|  \033[1;32;40m.  .\033[1;37;40m| \033[1;32;40m. \033[1;37;40m|")
                    print("\033[1;37;40m| || \033[1;32;40m.  .  .  .  . \033[1;37;40m__  \033[1;32;40m.  .  \033[1;37;40m| __===|_| |")
                    print("\033[1;37;40m| ||_______________||  \033[1;32;40m.  .  \033[1;37;40m|_|      | |")
                    print("\033[1;37;40m| ||_______\033[1;32;40mO.oooo\033[1;37;40m__||  \033[1;32;40m.  .  \033[1;37;40m| |______| |")
                    print("\033[1;37;40m| || \033[1;32;40m.  .  . O. Ooo\033[1;37;40m||  \033[1;32;40m.  .  \033[1;37;40m| |  |   | |")
                    print("\033[1;37;40m|---------------------------------------|")
                elif dots_random == 2:
                    print("\033[1;37;40m|---------------------------------------|")
                    print("\033[1;37;40m| \033[1;32;40m.  .  .  .  .  .  .  .  .  .  .  .  . \033[1;37;40m|")
                    print("\033[1;37;40m| \033[1;32;40m.  .  .  .  .  .  .  .  .  .  .  .  . \033[1;37;40m|")
                    print("\033[1;37;40m| \033[1;32;40m.  .  .  .  .  .  . O.  .  .  .  .  . \033[1;37;40m|")
                    print("\033[1;37;40m| __ \033[1;32;40m.  .  .  .  .  .ooo  .  \033[1;37;40m|  \033[1;32;40m.  .\033[1;37;40m| \033[1;32;40m. \033[1;37;40m|")
                    print("\033[1;37;40m| || \033[1;32;40m.  .  .  .  . \033[1;37;40m_\033[1;32;40mo o o .  \033[1;37;40m| __===|_| |")
                    print("\033[1;37;40m| ||_______________|| \033[1;32;40mo.  .  \033[1;37;40m|_|      | |")
                    print("\033[1;37;40m| ||_______________||\033[1;32;40mo o  .  \033[1;37;40m| |______| |")
                    print("\033[1;37;40m| || \033[1;32;40m.  .  .  .  . \033[1;37;40m||\033[1;32;40mo o  .  \033[1;37;40m| |  |   | |")
                    print("\033[1;37;40m|---------------------------------------|")
                elif dots_random == 3:
                    print("\033[1;37;40m|---------------------------------------|")
                    print("\033[1;37;40m| \033[1;32;40m.  .  .  .  .  .  .  .  .  .  .  .  . \033[1;37;40m|")
                    print("\033[1;37;40m| \033[1;32;40m.  .  .  .  .  .  .  .  .  .  .  .  . \033[1;37;40m|")
                    print("\033[1;37;40m| \033[1;32;40m.  .  .  .  .  .  .  .  .  .  O  .  . \033[1;37;40m|")
                    print("\033[1;37;40m| __ \033[1;32;40m.  .  .  .  .  .  .  .  \033[1;37;40m| \033[1;32;40mooo .\033[1;37;40m| \033[1;32;40m. \033[1;37;40m|")
                    print("\033[1;37;40m| || \033[1;32;40m.  .  .  .  . \033[1;37;40m__  \033[1;32;40m.  .  \033[1;37;40m|o__===|_| |")
                    print("\033[1;37;40m| ||_______________||  \033[1;32;40m.  .  \033[1;37;40m|_|      | |")
                    print("\033[1;37;40m| ||_______________||  \033[1;32;40m.  .  \033[1;37;40m| |______| |")
                    print("\033[1;37;40m| || \033[1;32;40m.  .  .  .  . \033[1;37;40m||  \033[1;32;40m.  .  \033[1;37;40m| |  |   | |")
                    print("\033[1;37;40m|---------------------------------------|")
                elif 3 < dots_random <= 40:
                    print("\033[1;37;40m|---------------------------------------|")
                    print("\033[1;37;40m| \033[1;32;40m.  .  .  .  .  .  .  .  .  .  .  .  . \033[1;37;40m|")
                    print("\033[1;37;40m| \033[1;32;40m.  .  .  .  .  .  .  .  .  .  .  .  . \033[1;37;40m|")
                    print("\033[1;37;40m| \033[1;32;40m.  .  .  .  .  .  .  .  .  .  .  .  . \033[1;37;40m|")
                    print("\033[1;37;40m| __ \033[1;32;40m.  .  .  .  .  .  .  .  \033[1;37;40m|  \033[1;32;40m.  .\033[1;37;40m| \033[1;32;40m. \033[1;37;40m|")
                    print("\033[1;37;40m| || \033[1;32;40m.  .  .  .  . \033[1;37;40m__  \033[1;32;40m.  .  \033[1;37;40m| __===|_| |")
                    print("\033[1;37;40m| ||_______________||  \033[1;32;40m.  .  \033[1;37;40m|_|      | |")
                    print("\033[1;37;40m| ||_______________||  \033[1;32;40m.  .  \033[1;37;40m| |______| |")
                    print("\033[1;37;40m| || \033[1;32;40m.  .  .  .  . \033[1;37;40m||  \033[1;32;40m.  .  \033[1;37;40m| |  |   | |")
                    print("\033[1;37;40m|---------------------------------------|")

def ghost_orbs(room):
    ghost_orbs_active = "true"
    while ghost_orbs_active == "true":
        ghost_orbs_action = input("\n\033[1;36;40morbs camera on (film/s): ")
        if ghost_orbs_action == "help":
            ghost_orbs_help()
        elif ghost_orbs_action == "stop":
            ghost_orbs_active = "false"
        elif ghost_orbs_action == "film" or ghost_orbs_action == "f":
            ghost_orbs_random = random.randint(0,25)
            if room == 0:
                if ghost_orbs_random == 0:
                    print("\033[1;37;40m|---------------------------------------|")
                    print("\033[1;37;40m|                           \033[1;38;40mo  \033[1;37;40m|        |")
                    print("\033[1;37;40m|          \033[1;38;40m.                   \033[1;37;40m|        |")
                    print("\033[1;37;40m|                              |____    |")
                    print("\033[1;37;40m|   \033[1;38;40mo                               \033[1;37;40m|   |")
                    print("\033[1;37;40m|                     \033[1;38;40m.         \033[1;37;40m___ |   |")
                    print("\033[1;37;40m| _____________    |          __|_|_|   |")
                    print("\033[1;37;40m|  |         |  ___|          |         |")
                    print("\033[1;37;40m|  |         |  |  |          |         |")
                    print("\033[1;37;40m|---------------------------------------|")
                elif ghost_orbs_random == 1:
                    print("\033[1;37;40m|---------------------------------------|")
                    print("\033[1;37;40m|                      \033[1;38;40mo       \033[1;37;40m|        |")
                    print("\033[1;37;40m|      \033[1;38;40m.                       \033[1;37;40m|        |")
                    print("\033[1;37;40m|                    \033[1;38;40m.         |\033[1;37;40m____    |")
                    print("\033[1;37;40m|            \033[1;38;40mo                      \033[1;37;40m|   |")
                    print("\033[1;37;40m|                               ___ |   |")
                    print("\033[1;37;40m| _____________    |          __|_|_|   |")
                    print("\033[1;37;40m|  |         |  ___|          |         |")
                    print("\033[1;37;40m|  |         |  |  |          |         |")
                    print("\033[1;37;40m|---------------------------------------|")
                elif ghost_orbs_random == 2:
                    print("\033[1;37;40m|---------------------------------------|")
                    print("\033[1;37;40m|                              |        |")
                    print("\033[1;37;40m|                  \033[1;38;40m.       o   \033[1;37;40m|        |")
                    print("\033[1;37;40m|        \033[1;38;40mo                     \033[1;37;40m|____    |")
                    print("\033[1;37;40m|                                   |   |")
                    print("\033[1;37;40m|                         \033[1;38;40m.     \033[1;37;40m___ |   |")
                    print("\033[1;37;40m| _____________    |          __|_|_|   |")
                    print("\033[1;37;40m|  |         |  ___|          |         |")
                    print("\033[1;37;40m|  |         |  |  |          |         |")
                    print("\033[1;37;40m|---------------------------------------|")
                elif ghost_orbs_random == 3:
                    print("\033[1;37;40m|         \033[1;38;40mo                    \033[1;37;40m|        |")
                    print("\033[1;37;40m|                \033[1;38;40m.             \033[1;37;40m|        |")
                    print("\033[1;37;40m|                         \033[1;38;40mo    \033[1;37;40m|____    |")
                    print("\033[1;37;40m|   \033[1;38;40m.                               \033[1;37;40m|   |")
                    print("\033[1;37;40m|                               ___ |   |")
                    print("\033[1;37;40m| _____________    |          __|_|_|   |")
                    print("\033[1;37;40m|  |         |  ___|          |         |")
                    print("\033[1;37;40m|  |         |  |  |          |         |")
                    print("\033[1;37;40m|---------------------------------------|")
                elif 3 < ghost_orbs_random <= 25:
                    print("\033[1;37;40m|---------------------------------------|")
                    print("\033[1;37;40m|                              |        |")
                    print("\033[1;37;40m|                              |        |")
                    print("\033[1;37;40m|                              |____    |")
                    print("\033[1;37;40m|                                   |   |")
                    print("\033[1;37;40m|                               ___ |   |")
                    print("\033[1;37;40m| _____________    |          __|_|_|   |")
                    print("\033[1;37;40m|  |         |  ___|          |         |")
                    print("\033[1;37;40m|  |         |  |  |          |         |")
                    print("\033[1;37;40m|---------------------------------------|")
                    print("\033[1;37;40m|---------------------------------------|")
            elif room == 1:
                if ghost_orbs_random == 0:
                    print("\033[1;37;40m|---------------------------------------|")
                    print("\033[1;37;40m|      \033[1;38;40mo                          .     \033[1;37;40m|")
                    print("\033[1;37;40m|                       \033[1;38;40mo    \033[1;37;40m_________  |")
                    print("\033[1;37;40m|   _________                |       |  |")
                    print("\033[1;37;40m|   |    \033[1;38;40m.  \033[1;37;40m|                |_______|  |")
                    print("\033[1;37;40m|   |_______|        ________|       |  |")
                    print("\033[1;37;40m|   |       |        |       |_______|  |")
                    print("\033[1;37;40m|   |_______|        |_______|       |  |")
                    print("\033[1;37;40m|   |       |        |       |_______|  |")
                    print("\033[1;37;40m|---------------------------------------|")
                elif ghost_orbs_random == 1:
                    print("\033[1;37;40m|---------------------------------------|")
                    print("\033[1;37;40m|    \033[1;38;40m.                   o              \033[1;37;40m|")
                    print("\033[1;37;40m|                            _________  |")
                    print("\033[1;37;40m|   _________           \033[1;38;40m.    \033[1;37;40m|       |  |")
                    print("\033[1;37;40m|   |       |   \033[1;38;40mo            \033[1;37;40m|_______|  |")
                    print("\033[1;37;40m|   |_______|        ________|       |  |")
                    print("\033[1;37;40m|   |       |        |       |_______|  |")
                    print("\033[1;37;40m|   |_______|        |_______|       |  |")
                    print("\033[1;37;40m|   |       |        |       |_______|  |")
                    print("\033[1;37;40m|---------------------------------------|")
                elif ghost_orbs_random == 2:
                    print("\033[1;37;40m|---------------------------------------|")
                    print("\033[1;37;40m|       \033[1;38;40mo                      .        \033[1;37;40m|")
                    print("\033[1;37;40m|                            _________  |")
                    print("\033[1;37;40m|   |       |    \033[1;38;40m.           \033[1;37;40m|_______|  |")
                    print("\033[1;37;40m|   |_______|        ________|   \033[1;38;40mo   \033[1;37;40m|  |")
                    print("\033[1;37;40m|   |       |        |       |_______|  |")
                    print("\033[1;37;40m|   |_______|        |_______|       |  |")
                    print("\033[1;37;40m|   |       |        |       |_______|  |")
                    print("\033[1;37;40m|---------------------------------------|")
                elif ghost_orbs_random == 3:
                    print("\033[1;37;40m|---------------------------------------|")
                    print("\033[1;37;40m|                               \033[1;38;40m.       \033[1;37;40m|")
                    print("\033[1;37;40m|    \033[1;38;40mo                      \033[1;37;40m _________  |")
                    print("\033[1;37;40m|   |       |        \033[1;38;40mo       \033[1;37;40m|_______|  |")
                    print("\033[1;37;40m|   |_______|        ________|       |  |")
                    print("\033[1;37;40m|   |       | \033[1;38;40m.      \033[1;37;40m|       |_______|  |")
                    print("\033[1;37;40m|   |_______|        |_______|       |  |")
                    print("\033[1;37;40m|   |       |        |       |_______|  |")
                    print("\033[1;37;40m|---------------------------------------|")
                elif 3 < ghost_orbs_random <= 25:
                    print("\033[1;37;40m|---------------------------------------|")
                    print("\033[1;37;40m|                                       |")
                    print("\033[1;37;40m|                            _________  |")
                    print("\033[1;37;40m|   |       |                |_______|  |")
                    print("\033[1;37;40m|   |_______|        ________|       |  |")
                    print("\033[1;37;40m|   |       |        |       |_______|  |")
                    print("\033[1;37;40m|   |_______|        |_______|       |  |")
                    print("\033[1;37;40m|   |       |        |       |_______|  |")
                    print("\033[1;37;40m|---------------------------------------|")
            elif room == 2:
                if ghost_orbs_random == 0:
                    print("\033[1;37;40m|---------------------------------------|")
                    print("\033[1;37;40m|                                       |")
                    print("\033[1;37;40m|  \033[1;38;40m.                              o     \033[1;37;40m|")
                    print("\033[1;37;40m|            \033[1;38;40mo                          \033[1;37;40m|")
                    print("\033[1;37;40m| __                         |      |   |")
                    print("\033[1;37;40m| ||               __   \033[1;38;40m.    \033[1;37;40m| __===|_| |")
                    print("\033[1;37;40m| ||_______________||        |_|      | |")
                    print("\033[1;37;40m| ||_______________||        | |______| |")
                    print("\033[1;37;40m| ||               ||        | |  |   | |")
                    print("\033[1;37;40m|---------------------------------------|")
                elif ghost_orbs_random == 1:
                    print("\033[1;37;40m|---------------------------------------|")
                    print("\033[1;37;40m|    \033[1;38;40m.                          o       \033[1;37;40m|")
                    print("\033[1;37;40m|                      \033[1;38;40m.                \033[1;37;40m|")
                    print("\033[1;37;40m|                                       |")
                    print("\033[1;37;40m| __      \033[1;38;40mo                  \033[1;37;40m|      |   |")
                    print("\033[1;37;40m| ||               __        | __===|_| |")
                    print("\033[1;37;40m| ||_______________||        |_|      | |")
                    print("\033[1;37;40m| ||_______________||        | |______| |")
                    print("\033[1;37;40m| ||               ||        | |  |   | |")
                    print("\033[1;37;40m|---------------------------------------|")
                elif ghost_orbs_random == 2:
                    print("\033[1;37;40m|---------------------------------------|")
                    print("\033[1;37;40m|                                  \033[1;38;40mo    \033[1;37;40m|")
                    print("\033[1;37;40m|                \033[1;38;40mo                      \033[1;37;40m|")
                    print("\033[1;37;40m|                         \033[1;38;40m.             \033[1;37;40m|")
                    print("\033[1;37;40m| __     \033[1;38;40m.                   \033[1;37;40m|      |   |")
                    print("\033[1;37;40m| ||               __        | __===|_| |")
                    print("\033[1;37;40m| ||_______________||        |_|      | |")
                    print("\033[1;37;40m| ||_______________||        | |______| |")
                    print("\033[1;37;40m| ||               ||        | |  |   | |")
                    print("\033[1;37;40m|---------------------------------------|")
                elif ghost_orbs_random == 3:
                    print("\033[1;37;40m|---------------------------------------|")
                    print("\033[1;37;40m|        \033[1;38;40mo                              \033[1;37;40m|")
                    print("\033[1;37;40m|                                  \033[1;38;40mo    \033[1;37;40m|")
                    print("\033[1;37;40m|                     \033[1;38;40m.                 \033[1;37;40m|")
                    print("\033[1;37;40m| __   \033[1;38;40m.                     \033[1;37;40m|      |   |")
                    print("\033[1;37;40m| ||               __        | __===|_| |")
                    print("\033[1;37;40m| ||_______________||        |_|      | |")
                    print("\033[1;37;40m| ||_______________||        | |______| |")
                    print("\033[1;37;40m| ||               ||        | |  |   | |")
                    print("\033[1;37;40m|---------------------------------------|")
                elif 3 < ghost_orbs_random <= 25:
                    print("\033[1;37;40m|---------------------------------------|")
                    print("\033[1;37;40m|                                       |")
                    print("\033[1;37;40m|                                       |")
                    print("\033[1;37;40m|                                       |")
                    print("\033[1;37;40m| __                         |      |   |")
                    print("\033[1;37;40m| ||               __        | __===|_| |")
                    print("\033[1;37;40m| ||_______________||        |_|      | |")
                    print("\033[1;37;40m| ||_______________||        | |______| |")
                    print("\033[1;37;40m| ||               ||        | |  |   | |")
                    print("\033[1;37;40m|---------------------------------------|")

#                                                   #NOT#
########################################################################################################################

def not_emf():
    emf_active = "true"
    while emf_active == "true":
        emf_action = input("\n\033[1;36;40memf on (scan/s): ")
        if emf_action == "help":
            emf_help()
        elif emf_action == "stop":
            emf_active = "false"
        elif emf_action == "scan" or emf_action == "s":
            emf_random = random.randint(0, 18)
            if 0 <= emf_random < 4:
                print("\033[1;37;40mo\033[1;37;40mo\033[1;37;40mo\033[1;37;40mo\033[1;37;40mo")
            elif 4 <= emf_random < 8:
                print("\033[1;34;40mo\033[1;37;40mo\033[1;37;40mo\033[1;37;40mo\033[1;37;40mo")
            elif 8 <= emf_random < 12:
                print("\033[1;34;40mo\033[1;36;40mo\033[1;37;40mo\033[1;37;40mo\033[1;37;40mo")
            elif 12 <= emf_random < 16:
                print("\033[1;34;40mo\033[1;36;40mo\033[1;32;40mo\033[1;37;40mo\033[1;37;40mo")
            elif 16 <= emf_random < 19:
                print("\033[1;34;40mo\033[1;36;40mo\033[1;32;40mo\033[1;33;40mo\033[1;37;40mo")

def not_freezing_temps():
    freezing_temps_active = "true"
    temp = random.randint(8, 14)
    while freezing_temps_active == "true":
        freezing_temps_action = input("\n\033[1;36;40mthermometer on (measure/m): \033[1;39;40m")
        if freezing_temps_action == "help":
            freezing_temps_help()
        elif freezing_temps_action == "stop":
            freezing_temps_active = "false"
        elif freezing_temps_action == "measure" or freezing_temps_action == "m":
            temp_change = random.randint(1, 3)
            if temp - temp_change < 1:
                temp += temp_change
            elif temp + temp_change > 14:
                temp -= temp_change
            else:
                temp_negative_positive = random.choice(["negative", "positive"])
                if temp_negative_positive == "negative":
                    temp -= temp_change
                else:
                    temp += temp_change
            if temp == 1 or temp == -1:
                print(temp, "degree celsius")
            else:
                print(temp, "degrees celsius")

def not_spirit_box():
    spirit_box_active = "true"
    while spirit_box_active == "true":
        spirit_box_action = input("\n\033[1;36;40mspirit box on: ")
        if spirit_box_action == "help":
            spirit_box_help()
        elif spirit_box_action == "stop":
            spirit_box_active = "false"
        elif spirit_box_action == "phrase list":
            phrase_list()
        else:
            print("** No response **")

def not_ultraviolet(random_ghost):
    ultraviolet_active = "true"
    while ultraviolet_active == "true":
        ultraviolet_action = input("\n\033[1;36;40multraviolet light on (look/l): ")
        if ultraviolet_action == "help":
            ultraviolet_help()
        elif ultraviolet_action == "stop":
            ultraviolet_active = "false"
        elif ultraviolet_action == "look" or ultraviolet_action == "l":
            if random_ghost == "wraith":
                random_ultraviolet = random.randint(0, 3)
            else:
                random_ultraviolet = random.randint(0, 4)
            if random_ultraviolet == 0:
                print("\033[1;39;40m __________________")
                print("\033[1;39;40m|   ____    ____   |")
                print("\033[1;39;40m|  |    |  |    |  |")
                print("\033[1;39;40m|  |    |  |    |  |")
                print("\033[1;39;40m|  |    |  |    |  |")
                print("\033[1;39;40m|  |____|  |____|  |")
                print("\033[1;39;40m|               @  |")
                print("\033[1;39;40m|   ____    ____   |")
                print("\033[1;39;40m|  |    |  |    |  |")
                print("\033[1;39;40m|  |    |  |    |  |")
                print("\033[1;39;40m|  |    |  |    |  |")
                print("\033[1;39;40m|  |____|  |____|  |")
                print("\033[1;39;40m|__________________|")
            elif random_ultraviolet == 1:
                print("\033[1;39;40m __________________")
                print("\033[1;39;40m|                  |")
                print("\033[1;39;40m|     ________     |")
                print("\033[1;39;40m|    |        |    |")
                print("\033[1;39;40m|    |        |    |")
                print("\033[1;39;40m|    |        |    |")
                print("\033[1;39;40m|    |________|    |")
                print("\033[1;39;40m|    |        |    |")
                print("\033[1;39;40m|    |        |    |")
                print("\033[1;39;40m|    |        |    |")
                print("\033[1;39;40m|    |________|    |")
                print("\033[1;39;40m|                  |")
                print("\033[1;39;40m|__________________|")
            elif random_ultraviolet == 2:
                print("\033[1;39;40m ___________________")
                print("\033[1;39;40m|    /    |    \\    |")
                print("\033[1;39;40m|   |     |     |   |")
                print("\033[1;39;40m|  /      |      \\  |")
                print("\033[1;39;40m| |_______|_______| |")
                print("\033[1;39;40m| |       |       | |")
                print("\033[1;39;40m|/        |        \\|")
                print("\033[1;39;40m|         |         |")
                print("\033[1;39;40m|_________|_________|")
            elif random_ultraviolet == 3:
                print("\033[1;39;40m ____________")
                print("\033[1;39;40m|   ______   |")
                print("\033[1;39;40m|   ______   |")
                print("\033[1;39;40m||           |")
                print("\033[1;39;40m|            |")
                print("\033[1;39;40m|            |")
                print("\033[1;39;40m|        |@| |")
                print("\033[1;39;40m|            |")
                print("\033[1;39;40m|            |")
                print("\033[1;39;40m|            |")
                print("\033[1;39;40m|            |")
                print("\033[1;39;40m|   ______   |")
                print("\033[1;39;40m|____________|")
            elif random_ultraviolet == 4:
                print("\033[1;39;40m      ____________   _                      .  ________________")
                print("\033[1;39;40m  ___/          _/ _ .                       _ . \\__           \\_____")
                print("\033[1;39;40m /           __/ . _                             .. \\___             \\")
                print("\033[1;39;40m|           /_  ..                                .   _  \\            |")
                print("\033[1;39;40m|          | _ .  .                                 . . _ |         _/")
                print("\033[1;39;40m \\___       \\_ . -                                . .  __/        _/")
                print("\033[1;39;40m     \\___    \\__ .  .                          .  _ __/      ____/")
                print("\033[1;39;40m         \\______\\_ . _                     .   _  ./________/")

def not_ghost_writing():
    ghost_writing_active = "true"
    while ghost_writing_active == "true":
        ghost_writing_action = input("\n\033[1;36;40mbook in hand (place/p): ")
        if ghost_writing_action == "help":
            ghost_writing_help()
        elif ghost_writing_action == "stop":
            ghost_writing_active = "false"
        elif ghost_writing_action == "place" or ghost_writing_action == "p":
            print("\033[1;35;40m _______________/---\\_______________")
            print("\033[1;39;40m|                 |                 |")
            print("\033[1;39;40m|                 |                 |")
            print("\033[1;39;40m|                 |                 |")
            print("\033[1;39;40m|                 |                 |")
            print("\033[1;39;40m|                 |                 |")
            print("\033[1;39;40m|                 |                 |")
            print("\033[1;39;40m|\033[1;35;40m________________/ \\________________\033[1;39;40m|")

def not_dots(room):
    dots_active = "true"
    while dots_active == "true":
        dots_action = input("\n\033[1;36;40mdots on (watch/w): ")
        if dots_action == "help":
            dots_help()
        elif dots_action == "stop":
            dots_active = "false"
        elif dots_action == "watch" or dots_action == "w":
            if room == 0:
                print("\033[1;37;40m|---------------------------------------|")
                print("\033[1;37;40m| \033[1;32;40m.  .  .  .  .  .  .  .  .  . \033[1;37;40m|        |")
                print("\033[1;37;40m| \033[1;32;40m.  .  .  .  .  .  .  .  .  . \033[1;37;40m|        |")
                print("\033[1;37;40m| \033[1;32;40m.  .  .  .  .  .  .  .  .  . \033[1;37;40m|____    |")
                print("\033[1;37;40m| \033[1;32;40m.  .  .  .  .  .  .  .  .  .  .  .\033[1;37;40m|   |")
                print("\033[1;37;40m| \033[1;32;40m.  .  .  .  .  .  .  .  .  .  \033[1;37;40m___ |   |")
                print("\033[1;37;40m| _____________  \033[1;32;40m. \033[1;37;40m|\033[1;32;40m.  .  .  .\033[1;37;40m__|_|_|   |")
                print("\033[1;37;40m|  | \033[1;32;40m.  .  . \033[1;37;40m|  ___|\033[1;32;40m.  .  .  .\033[1;37;40m|         |")
                print("\033[1;37;40m|  | \033[1;32;40m.  .  . \033[1;37;40m|  |  |\033[1;32;40m.  .  .  .\033[1;37;40m|         |")
                print("\033[1;37;40m|---------------------------------------|")
            elif room == 1:
                print("\033[1;37;40m|---------------------------------------|")
                print("\033[1;37;40m| \033[1;32;40m.  .  .  .  .  .  .  .  .  .  .  .  . \033[1;37;40m|")
                print("\033[1;37;40m| \033[1;32;40m.  .  .  .  .  .  .  .  .  \033[1;37;40m_________\033[1;32;40m. \033[1;37;40m|")
                print("\033[1;37;40m| \033[1;32;40m. \033[1;37;40m_________ \033[1;32;40m.  .  .  .  .  \033[1;37;40m|  \033[1;32;40m.  . \033[1;37;40m|\033[1;32;40m. \033[1;37;40m|")
                print("\033[1;37;40m| \033[1;32;40m. \033[1;37;40m|\033[1;32;40m.  .  .\033[1;37;40m| \033[1;32;40m.  .  .  .  .  \033[1;37;40m|_______|\033[1;32;40m. \033[1;37;40m|")
                print("\033[1;37;40m| \033[1;32;40m. \033[1;37;40m|_______| \033[1;32;40m.  .  .\033[1;37;40m________|  \033[1;32;40m.  . \033[1;37;40m|\033[1;32;40m. \033[1;37;40m|")
                print("\033[1;37;40m| \033[1;32;40m. \033[1;37;40m|\033[1;32;40m.  .  .\033[1;37;40m| \033[1;32;40m.  .  .\033[1;37;40m| \033[1;32;40m.  .  \033[1;37;40m|_______|\033[1;32;40m. \033[1;37;40m|")
                print("\033[1;37;40m| \033[1;32;40m. \033[1;37;40m|_______| \033[1;32;40m.  .  .\033[1;37;40m|_______|  \033[1;32;40m.  . \033[1;37;40m|\033[1;32;40m. \033[1;37;40m|")
                print("\033[1;37;40m| \033[1;32;40m. \033[1;37;40m|\033[1;32;40m.  .  .\033[1;37;40m| \033[1;32;40m.  .  .\033[1;37;40m| \033[1;32;40m.  .  \033[1;37;40m|_______|\033[1;32;40m. \033[1;37;40m|")
                print("\033[1;37;40m|---------------------------------------|")
            elif room == 2:
                print("\033[1;37;40m|---------------------------------------|")
                print("\033[1;37;40m| \033[1;32;40m.  .  .  .  .  .  .  .  .  .  .  .  . \033[1;37;40m|")
                print("\033[1;37;40m| \033[1;32;40m.  .  .  .  .  .  .  .  .  .  .  .  . \033[1;37;40m|")
                print("\033[1;37;40m| \033[1;32;40m.  .  .  .  .  .  .  .  .  .  .  .  . \033[1;37;40m|")
                print("\033[1;37;40m| __ \033[1;32;40m.  .  .  .  .  .  .  .  \033[1;37;40m|  \033[1;32;40m.  .\033[1;37;40m| \033[1;32;40m. \033[1;37;40m|")
                print("\033[1;37;40m| || \033[1;32;40m.  .  .  .  . \033[1;37;40m__  \033[1;32;40m.  .  \033[1;37;40m| __===|_| |")
                print("\033[1;37;40m| ||_______________||  \033[1;32;40m.  .  \033[1;37;40m|_|      | |")
                print("\033[1;37;40m| ||_______________||  \033[1;32;40m.  .  \033[1;37;40m| |______| |")
                print("\033[1;37;40m| || \033[1;32;40m.  .  .  .  . \033[1;37;40m||  \033[1;32;40m.  .  \033[1;37;40m| |  |   | |")
                print("\033[1;37;40m|---------------------------------------|")

def not_ghost_orbs(room):
    ghost_orbs_active = "true"
    while ghost_orbs_active == "true":
        ghost_orbs_action = input("\n\033[1;36;40morbs camera on (film/f): ")
        if ghost_orbs_action == "help":
            ghost_orbs_help()
        elif ghost_orbs_action == "stop":
            ghost_orbs_active = "false"
        elif ghost_orbs_action == "film" or ghost_orbs_action == "f":
            if room == 0:
                print("\033[1;37;40m|---------------------------------------|")
                print("\033[1;37;40m|                              |        |")
                print("\033[1;37;40m|                              |        |")
                print("\033[1;37;40m|                              |____    |")
                print("\033[1;37;40m|                                   |   |")
                print("\033[1;37;40m|                               ___ |   |")
                print("\033[1;37;40m| _____________    |          __|_|_|   |")
                print("\033[1;37;40m|  |         |  ___|          |         |")
                print("\033[1;37;40m|  |         |  |  |          |         |")
                print("\033[1;37;40m|---------------------------------------|")
                print("\033[1;37;40m|---------------------------------------|")
            elif room == 1:
                print("\033[1;37;40m|---------------------------------------|")
                print("\033[1;37;40m|                                       |")
                print("\033[1;37;40m|                            _________  |")
                print("\033[1;37;40m|   |       |                |_______|  |")
                print("\033[1;37;40m|   |_______|        ________|       |  |")
                print("\033[1;37;40m|   |       |        |       |_______|  |")
                print("\033[1;37;40m|   |_______|        |_______|       |  |")
                print("\033[1;37;40m|   |       |        |       |_______|  |")
                print("\033[1;37;40m|---------------------------------------|")
            elif room == 2:
                print("\033[1;37;40m|---------------------------------------|")
                print("\033[1;37;40m|                                       |")
                print("\033[1;37;40m|                                       |")
                print("\033[1;37;40m|                                       |")
                print("\033[1;37;40m| __                         |      |   |")
                print("\033[1;37;40m| ||               __        | __===|_| |")
                print("\033[1;37;40m| ||_______________||        |_|      | |")
                print("\033[1;37;40m| ||_______________||        | |______| |")
                print("\033[1;37;40m| ||               ||        | |  |   | |")
                print("\033[1;37;40m|---------------------------------------|")

#                                                  #OTHER#
########################################################################################################################

def ghost_randomizer():
    ghost_types_list = ["spirit", "wraith", "phantom", "poltergeist", "banshee", "jinn", "mare", "revenant", "shade", "demon", "yurei", "oni", "hantu", "yokai", "goryo", "myling", "onryo", "twins", "raiju", "obake", "mimic", "moroi", "deogen", "thaye"]
    random_ghost = random.choice(ghost_types_list)
    return random_ghost

def intro():
    print("\033[1;35;40mWelcome to Phasmophobia Python Edition! \n")
    print("\033[1;36;40m** Tip: Grab a pen and paper so you can write down what evidence you've gotten **")
    print("\033[1;36;40m** This game is case sensitive, everything will be lowercase ** ")
    print("\033[1;36;40m** If you have any typos it will just ask you the same question again ** \n")
    print("\033[1;34;40mIn this game you're supposed to figure out what ghost is haunting your house.")
    print("You will be asked what you want to do and you have 9 options")
    print("To find evidence you can say \033[1;35;40memf, freezing temps, ultraviolet, spirit box, ghost writing, dots, or ghosts orbs.")
    print("\033[1;34;40mWhen trying to find evidence you can say \033[1;35;40mhelp \033[1;34;40mto get an explanation on how to use the tool; \033[1;35;40mstop \033[1;34;40mto stop using")
    print("the tool and go back; or whatever the given action keyword for the tool you're using is")
    print("\033[1;34;40mYou can also say \033[1;35;40mguess \033[1;34;40mto guess the ghost; \033[1;35;40mghosts \033[1;34;40mto see what the ghosts are and what evidence each one has again\033[1;38;40m \n")

def ghost_list():
    print("\033[1;35;40mspirit:        \033[1;34;40memf          \033[1;35;40m|   \033[1;34;40mspirit box     \033[1;35;40m|   \033[1;34;40mghost writing")
    print("\033[1;35;40mwraith:        \033[1;34;40memf          \033[1;35;40m|   \033[1;34;40mspirit box     \033[1;35;40m|   \033[1;34;40mbots")
    print("\033[1;35;40mphantom:       \033[1;34;40mspirit box   \033[1;35;40m|   \033[1;34;40multraviolet    \033[1;35;40m|   \033[1;34;40mdots")
    print("\033[1;35;40mpoltergeist:   \033[1;34;40mspirit box   \033[1;35;40m|   \033[1;34;40multraviolet    \033[1;35;40m|   \033[1;34;40mghost writing")
    print("\033[1;35;40mbanshee:       \033[1;34;40multraviolet  \033[1;35;40m|   \033[1;34;40mghost orbs     \033[1;35;40m|   \033[1;34;40mdots")
    print("\033[1;35;40mjinn:          \033[1;34;40memf          \033[1;35;40m|   \033[1;34;40multraviolet    \033[1;35;40m|   \033[1;34;40mfreezing temps")
    print("\033[1;35;40mmare:          \033[1;34;40mspirit box   \033[1;35;40m|   \033[1;34;40mghost orbs     \033[1;35;40m|   \033[1;34;40mghost writing")
    print("\033[1;35;40mrevenant:      \033[1;34;40mghost orbs   \033[1;35;40m|   \033[1;34;40mghost writing  \033[1;35;40m|   \033[1;34;40mfreezing temps")
    print("\033[1;35;40mshade:         \033[1;34;40memf          \033[1;35;40m|   \033[1;34;40mghost writing  \033[1;35;40m|   \033[1;34;40mfreezing temps")
    print("\033[1;35;40mdemon:         \033[1;34;40multraviolet  \033[1;35;40m|   \033[1;34;40mghost writing  \033[1;35;40m|   \033[1;34;40mfreezing temps")
    print("\033[1;35;40myurei:         \033[1;34;40mghost orbs   \033[1;35;40m|   \033[1;34;40mdots           \033[1;35;40m|   \033[1;34;40mfreezing temps")
    print("\033[1;35;40moni:           \033[1;34;40memf          \033[1;35;40m|   \033[1;34;40mdots           \033[1;35;40m|   \033[1;34;40mfreezing temps")
    print("\033[1;35;40mhantu:         \033[1;34;40multraviolet  \033[1;35;40m|   \033[1;34;40mghost orbs     \033[1;35;40m|   \033[1;34;40mfreezing temps")
    print("\033[1;35;40myokai:         \033[1;34;40mspirit box   \033[1;35;40m|   \033[1;34;40mghost orbs     \033[1;35;40m|   \033[1;34;40mdots")
    print("\033[1;35;40mgoryo:         \033[1;34;40memf          \033[1;35;40m|   \033[1;34;40multraviolet    \033[1;35;40m|   \033[1;34;40mdots")
    print("\033[1;35;40mmyling:        \033[1;34;40memf          \033[1;35;40m|   \033[1;34;40multraviolet    \033[1;35;40m|   \033[1;34;40mghost writing")
    print("\033[1;35;40monryo:         \033[1;34;40mspirit box   \033[1;35;40m|   \033[1;34;40mghost orbs     \033[1;35;40m|   \033[1;34;40mfreezing temps")
    print("\033[1;35;40mtwins:         \033[1;34;40memf          \033[1;35;40m|   \033[1;34;40mspirit box     \033[1;35;40m|   \033[1;34;40mfreezing temps")
    print("\033[1;35;40mraiju:         \033[1;34;40memf          \033[1;35;40m|   \033[1;34;40mghost orbs     \033[1;35;40m|   \033[1;34;40mdots")
    print("\033[1;35;40mobake:         \033[1;34;40memf          \033[1;35;40m|   \033[1;34;40multraviolet    \033[1;35;40m|   \033[1;34;40mghost orbs")
    print("\033[1;35;40mmoroi:         \033[1;34;40mspirit box   \033[1;35;40m|   \033[1;34;40mghost writing  \033[1;35;40m|   \033[1;34;40mfreezing temps")
    print("\033[1;35;40mdeogen:        \033[1;34;40mspirit box   \033[1;35;40m|   \033[1;34;40mghost writing  \033[1;35;40m|   \033[1;34;40mdots")
    print("\033[1;35;40mthaye:         \033[1;34;40mghost orbs   \033[1;35;40m|   \033[1;34;40mghost writing  \033[1;35;40m|   \033[1;34;40mdots")
    print("\033[1;35;40mmimic:         \033[1;34;40mspirit box   \033[1;35;40m|   \033[1;34;40multraviolet    \033[1;35;40m|   \033[1;34;40mfreezing temps")

def guess(random_ghost):
    guessing = "true"
    while guessing == "true":
        guessed_ghost = input("\033[1;35;36mWhat is your guess? ")
        if guessed_ghost == random_ghost:
            guessing = "false"
            print("\033[1;33;40mYou did it!!!")
        elif guessed_ghost in ["spirit","wraith","phantom","banshee","jinn","mare","revenant","shade","demon","yurei","oni","hantu","yokai","goryo","myling","onryo","twins","raiju","obake","mimic","moroi","deogen","thaye"]:
            guessing = "false"
            print("\033[1;31;40mYOU DIE")
            print("The correct ghost was " + random_ghost)

def end_game():
    game_over = "false"
    play_again = input("\033[1;36;40mWould you like to play again? (yes or no) ")
    if play_again == "no":
        game_over = "true"
        print("\033[1;33;40mHave a great day!")
    return game_over

#                                                    #MAIN#
########################################################################################################################

def main():
    game_over = "false"
    round_ghost = ghost_randomizer()
    random_room = random.randint(0,2)
    ghost_age = random.randint(3,70)

    intro()
    ghost_list()
    print(round_ghost)# this is just for testing remove when done -----------------------------------------------------

    while game_over == "false":
        action = input("\n\033[1;35;40mWhat would you like to do? \033[1;38;40m")

        if action == "emf":
            if round_ghost in ["spirit","wraith","jinn","shade","oni","goryo","myling","twins","raiju","obake"]:
                emf()
            else:
                not_emf()

        elif action == "freezing temps":
            if round_ghost in ["jinn","revenant","shade","demon","yurei","oni","hantu","onryo","twins","moroi","deogen"]:
                freezing_temps()
            else:
                not_freezing_temps()

        elif action == "spirit box":
            if round_ghost in ["spirit","wraith","phantom","poltergeist","mare","yokai","onryo","twins","mimic","moroi","deogen"]:
                spirit_box(ghost_age)
            else:
                not_spirit_box()

        elif action == "ultraviolet":
            if round_ghost in ["phantom","poltergeist","banshee","jinn","demon","hantu","goryo","myling","obake","mimic"]:
                ultraviolet(round_ghost)
            else:
                not_ultraviolet(round_ghost)

        elif action == "ghost writing":
            if round_ghost in ["spirit","poltergeist","mare","revenant","shade","demon","myling","moroi","deogen","thaye"]:
                ghost_writing()
            else:
                not_ghost_writing()

        elif action == "dots":
            if round_ghost in ["wraith","phantom","banshee","yurei","oni","yokai","goryo","raiju","deogen","thaye"]:
                dots(random_room)
            else:
                not_dots(random_room)

        elif action == "ghost orbs":
            if round_ghost in ["banshee","mare","revenant","yurei","hantu","yokai","onryo","raiju","obake","mimic","thaye"]:
                ghost_orbs(random_room)
            else:
                not_ghost_orbs(random_room)


        elif action == "ghosts":
            ghost_list()

        elif action == "guess":
            guess(round_ghost)
            round_ghost = ghost_randomizer()
            game_over = end_game()


if __name__ == "__main__":
    main()