import time # Idea came from Unity coroutines
from game_manager import start_game
from menu_funcs import pre_game,exit_app,powerup_chooser,show_inventory,name_change,show_credits,invalid_com
from text_reader import read_text
from classes_powerup_handler import item_list_creator, area_list_creator, player_creator
from game_data import game_load

minor_border = 12

player = None
item_collection = []
area_list = []
area = ""

menu_input = ""
powerup_inventory = []
selected_powerup = ""
inventory_limit = 2
skip_flag = False
powerup_taken = False

# Takes the list of items and areas and assigns them to global variables to be used throughout the program
# Uses the functions to create list of areas and items
def object_assignment(area):
    global item_collection,area_list

    item_collection = item_list_creator()
    area_list = area_list_creator(item_collection,area)
    
# Creates the player object
def player_assignment():
    global player
    player = player_creator(player,user_name,area_list,powerup_inventory,area,powerup_taken) 

# This part contains the outer part of the game as in the main menu functionality and game launching code.
# Prevents players under 12 (k-12)
# Reads files
# Calls relevant functions when running the game such as starting new game, loading the game etc and handles the Main Menu paths as well.
read_text("intro.txt")
time.sleep(3)
read_text("rules.txt")
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
            if powerup_inventory == []:
                print("\nDisclaimer: You have started without choosing any powerups! It can be still chosen from the Main menu")
                time.sleep(2)
            user_pre = pre_game()

            while command_started != True:

                if user_pre == "n":
                    command_started = True
                    route_chosen = False

                    while route_chosen == False:
                        area_raw = str(input("\nChoose your route: Neighborhood\t\tDownTown\tOutdoors\n"))
                        area = area_raw.lower()

                        if area == "neighborhood" or area == "downtown" or area == "outdoors":
                            object_assignment(area)
                            route_chosen = True
                        else:
                            print("No such route exists!")

                    player_assignment()
                    start_game(player,user_name,user_age,area_list,selected_powerup,skip_flag)

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
                        object_assignment(player.area)
                        start_game(player,user_name,user_age,area_list,selected_powerup,skip_flag)
                        

                elif user_pre == "e":
                    command_started = True
                    exit_app()

                else:
                    print("\nInvalid Command! Try Again!")
                    time.sleep(1)
                    user_pre = pre_game()

        elif menu_input == "p":
            read_text("powerup_info.txt")
            time.sleep(5)
            powerup_chooser(powerup_inventory,inventory_limit,powerup_taken)
            powerup_taken = True

        elif menu_input == "i":
            show_inventory(powerup_inventory)
                
        elif menu_input == "n":
            user_name = name_change()

        elif menu_input == "r":
            read_text("rules.txt")
            time.sleep(10)

        elif menu_input == "c":
            show_credits()

        elif menu_input == "lopeta":
            exit_app()

        else:
            invalid_com()

        
        