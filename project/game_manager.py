import time
from classes_powerup_handler import powerup_choice, powerup_usage
from game_data import game_save
from menu_funcs import exit_app

# Code when the game ends
def game_ender(user_name,user_age,player):
    global game_ended 
    exit_input_raw = str(input("\nEnter command: "))
    exit_input = exit_input_raw.lower()

    if exit_input == "y":
        if player != None:
            print("\nSaving game...")
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
    

# This code contains the internal part (Game Menu) of the game which starts when the game is started from the Main Menu
def start_game(player,user_name,user_age,area_list,selected_powerup,skip_flag):

    def movement_inp():
            print(f"\nYou are currently at {player.location.name}.\n\nEnter W to move to the next location\nEnter E to end game")
            user_mov_raw = str(input("\nEnter command: "))
            user_mov_com = user_mov_raw.lower()
            return user_mov_com
    
    def item_dealing(selected_powerup,skip_flag):

        print(f"\nEntering {player.location.name}..")
        time.sleep(1)
        print(f"You entered {player.location.name}!")
        time.sleep(1)
        print(f"\nYou have encountered an item!")
        time.sleep(1)
        print(f"\nAnalyzing the item....")
        time.sleep(2)
        print(f"\nHint: {player.location.item.riddle}")
        print(f"Weight of the item is {player.location.item.weight} grams")
        time.sleep(2)

        if player.powerup_inventory != []:
            selected_powerup = powerup_choice(player.powerup_inventory)

            if selected_powerup != "":
                skip_flag = powerup_usage(selected_powerup,player)

        if skip_flag == False:
            time.sleep(5)
            user_decision_raw = str(input("\nEnter T to throw it in the dustbin\tEnter R to report it to the police!\n"))
            user_decision_com = user_decision_raw.lower()
            return user_decision_com

        else:
            return ""
    
    print("\nLoading Game...")
    time.sleep(2)
    print("\nLoading..")
    time.sleep(1)
    print("\nLoading.")
    time.sleep(1)
    print("\nGame Started!")
    time.sleep(1)


    user_mov = movement_inp()
    game_ended = False
    item_dealt = False
    i = 0

    for n in area_list:
        if n.name == player.location.name:
            i = area_list.index(n)

    while i >= 0 and i < len(area_list) - 1:
        if user_mov == "w":
            player.location = area_list[i+1]

            while item_dealt == False:
                user_decision = item_dealing(selected_powerup,skip_flag)

                if user_decision == "t":
                    item_dealt = True

                    if player.location.item.trash == True:
                        print("\nYou have guessed right! You get Citizen points.")
                        player.citizen_points += 10
                        time.sleep(1)
                        print(f"\nCurrent Citizen life: {player.citizen_life}")
                        print(f"Current Citizen points: {player.citizen_points}")
                        time.sleep(2)
                    else:
                        print(f"\nYou threw someone's {player.location.item.name} in the trash and now they might never find it! Citizen life deducted!")
                        player.citizen_life -= 10
                        time.sleep(1)
                        print(f"\nCurrent Citizen life: {player.citizen_life}")
                        print(f"Current Citizen points: {player.citizen_points}")
                        time.sleep(2)

                elif user_decision == "r":
                    item_dealt = True

                    if player.location.item.trash == False:
                        print("\nYou have guessed right! You get Citizen points.")
                        player.citizen_points += 10
                        time.sleep(1)
                        print(f"\nCurrent Citizen life: {player.citizen_life}")
                        print(f"Current Citizen points: {player.citizen_points}")
                        time.sleep(2)
                    else:
                        print(f"\nPolice officer: Why did you bring {player.location.item.name} here?! Citizen life deducted!")
                        player.citizen_life -= 10
                        time.sleep(1)
                        print(f"\nCurrent Citizen life: {player.citizen_life}")
                        print(f"Current Citizen points: {player.citizen_points}")
                        time.sleep(2)

                elif user_decision == "" and skip_flag == True:
                    item_dealt = True

                else:
                    print("\nInvalid Command! Try Again.")
                    

            if player.citizen_life <= 0:
                print(f"\nSadly your global citizen life ends here! Final score: {player.citizen_points}. Good luck next time!")

                while game_ended == False:
                    print("\nDo you wish to save your points before exiting?\nEnter Y to save game\nEnter N to exit without saving")
                    game_ender(game_ended,user_name,user_age,player)
            else:
                i += 1
                item_dealt = False
                skip_flag = False
                user_mov = movement_inp()

        elif user_mov == "e":
            
            while game_ended == False: 
                print("\nDo you wish to save the game before exiting?\nEnter Y to save game\nEnter N to exit without saving")
                game_ender(game_ended,user_name,user_age,player)
                
            print("\nReturning to Main Menu!")
            
        else:
            print("\nInvalid Command! Try Again!")
            time.sleep(1)
            user_mov = movement_inp()

    print("Congratulations!!!! You are the Ultimate Global Citizen !!!!")
    while game_ended == False: 
        print("\nDo you wish to save the game before exiting?\nEnter Y to save game\nEnter N to exit without saving")
        game_ender(game_ended,user_name,user_age,player)
    

    