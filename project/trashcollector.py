import time 
from gamestarter_package import item_list_creator,room_list_creator,player_creator,start_game
from menu_package import pre_game,exit_app,powerup_chooser,show_inventory,name_change,show_credits,invalid_com
from intro_package import show_intro, show_rules
from gamedata_package import game_load,game_save

minor_border = 12


player = None
item_collection = []
room_list = []

menu_input = ""
powerup_inventory = []
inventory_limit = 2
trashbag = []

def object_assignment():
    global item_collection,room_list

    item_collection = item_list_creator()
    room_list = room_list_creator(item_collection)
    

def player_assignment():
    global player
    player = player_creator(player,user_name,trashbag,room_list)

# Main
show_intro("intro.txt")
time.sleep(1)
show_rules("rules.txt")
time.sleep(1)
user_name = str(input("\nEnter Your Name: "))
user_age = int(input("Enter Your Age: "))
print(f"\nName: {user_name}")
print(f"Age: {user_age}")

if user_age < minor_border:
    print("\nYou are a minor and this game is not for minors! Exiting application..")
    time.sleep(2)

else:
    print(f"\nWelcome {user_name}! Loading Main Menu...")
    while menu_input != "lopeta":
        time.sleep(2)
        print("\nMain Menu\n\nEnter S to Start\n\nEnter P to choose your powerups\n\nEnter I to show Powerup Inventory\n\nEnter N to change name\n\nEnter R to rules\n\nEnter C for Credits\n\nEnter lopeta to exit")
        menu_input_raw = str(input("\nEnter command: "))
        menu_input = menu_input_raw.lower()
    
        if menu_input == "s":

            command_started = False
            user_pre = pre_game()

            while command_started != True:

                if user_pre == "n":
                    command_started = True
                    object_assignment()
                    player_assignment()
                    start_game(player,item_collection,room_list)

                elif user_pre == "l":
                    player = game_load(user_name,user_age)

                    if player == None:
                        command_started = False
                        time.sleep(1)
                        user_pre = pre_game()

                    else:
                        command_started = True
                        print("\nContinuing from previous save..")
                        time.sleep(1)
                        object_assignment()
                        start_game(player,item_collection,room_list)
                        

                elif user_pre == "e":
                    command_started = True
                    exit_app()

                else:
                    print("\nInvalid Command! Try Again!")
                    time.sleep(1)
                    user_pre = pre_game()

        elif menu_input == "p":
            powerup_chooser(powerup_inventory,inventory_limit)

        elif menu_input == "i":
            show_inventory(powerup_inventory)
                
        elif menu_input == "n":
            user_name = name_change()

        elif menu_input == "r":
            show_rules("rules.txt")
            time.sleep(10)

        elif menu_input == "c":
            show_credits()

        elif menu_input == "lopeta":

            game_ended = False

            while game_ended == False: 
                print("Do you wish to save the game before exiting?\nEnter Y to save game\nEnter N to exit without saving")
                exit_input_raw = str(input("\nEnter command: "))
                exit_input = exit_input_raw.lower()

                if exit_input == "y":
                    if player != None:
                        print("Saving game...")
                        game_save(user_name,user_age,player)
                        time.sleep(1)
                        print("Game saved!")
                        game_ended = True
                        exit_app()

                    else:
                        print("As game was not started, there was no data to save!")
                        game_ended = True
                        exit_app()

                elif exit_input == "n":
                    game_ended = True
                    exit_app()

                else:
                    print("\nInvalid Command! Try Again!")

        else:
            invalid_com()

        
        