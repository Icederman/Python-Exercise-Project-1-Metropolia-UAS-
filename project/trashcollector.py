import time # Idea came from Unity coroutines
from gamestarter_package import item_list_creator,room_list_creator,player_creator,start_game
from menu_package import pre_game,exit_app,powerup_chooser,show_inventory,name_change,show_credits,invalid_com
from intro_package import show_intro, show_rules
from gamedata_package import game_load

minor_border = 12

player = None
item_collection = []
room_list = []

menu_input = ""
powerup_inventory = []
inventory_limit = 2
trashbag = []

# Takes the list of items and rooms and assigns them to global variables to be used throughout the program
def object_assignment():
    global item_collection,room_list

    item_collection = item_list_creator()
    room_list = room_list_creator(item_collection)
    
# Creates the player object
def player_assignment():
    global player
    player = player_creator(player,user_name,room_list) 

# This part contains the outer part of the game as in the main menu functionality and game launching code.
show_intro("intro.txt")
time.sleep(3)
show_rules("rules.txt")
time.sleep(15)

user_name = str(input("\nEnter Your Name: "))
while user_name == "":
    print("You have to enter a name!")
    user_name = str(input("\nEnter Your Name: "))
   
correct_age = False

while correct_age == False:
    try:
        user_age = int(input("Enter Your Age: "))

    except ValueError:
        print("\nAge needs to be an integer")
        correct_age = False

    else:
        correct_age = True

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
                    start_game(player,user_name,user_age,room_list)

                elif user_pre == "l":
                    player = game_load(user_name,user_age)

                    if player == None:
                        command_started = False
                        time.sleep(1)
                        user_pre = pre_game()

                    elif player.citizen_life <= 0:
                        print(f"Your previous score: {player.citizen_life}")

                    else:
                        command_started = True
                        print("\nContinuing from previous save..")
                        time.sleep(1)
                        object_assignment()
                        start_game(player,user_name,user_age,room_list)
                        

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
            exit_app()

        else:
            invalid_com()

        
        