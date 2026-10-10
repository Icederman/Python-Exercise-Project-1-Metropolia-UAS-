import time
import main_classes
from gamedata_package import game_save
from menu_package import exit_app


# Creates the items meant for the rooms and returns a list of those items
def item_list_creator():

    item_1 = main_classes.Item("Banana peel", "Yellow, curved, slippery on the inside.", 30)
    item_2 = main_classes.Item("Candy wrapper", "Thin, shiny, crinkles when squeezed, twisted at both ends.", 5)
    item_3 = main_classes.Item("Wallet", "Brown, rectangular, folds in half, has slots inside", 200, False)
    item_4 = main_classes.Item("Old newspaper", "Gray, flat, small black marks, a date and headlines at the top.", 150)
    item_5 = main_classes.Item("Diamond necklace", "Shiny, cold to the touch, hangs from a chain, has a clear stone.",30, False)
    item_6 = main_classes.Item("Gold coin", "Round, yellow, heavy for its size, a face on one side.",31, False)
    item_7 = main_classes.Item("Empty cereal box", "Rectangular, light, bright colors, a list of numbers on the side.",90)
    item_8 = main_classes.Item("Soda can", "Cylindrical, metallic, cold, a ring on top.",15)
    item_9 = main_classes.Item("Dead battery", "Small cylinder, a metal end, a symbol printed near the top.",23)
    item_10 = main_classes.Item("Toilet paper", "White, soft, wound around a hollow core.",100)
    item_11 = main_classes.Item("Passport", "Small, rectangular, many thin pages, stamped in several places.",40, False)
    item_12 = main_classes.Item("Old shoe", "One of a pair, flexible, worn down on one side.",400)
    item_13 = main_classes.Item("Smartphone", "Flat, smooth, dark until touched.",190, False)
    item_14 = main_classes.Item("Watch", "Circular, metallic, repeats the same motion all day.",150, False)
    item_15 = main_classes.Item("Bread", "Firm on the outside, full of tiny holes on the inside.",70)
    return [item_1,item_2,item_3,item_4,item_5,item_6,item_7,item_8,item_9,item_10,item_11,item_12,item_13,item_14,item_15]

# Creates rooms of the game and returns the list of those rooms
def room_list_creator(item_collection):
    room_0 = main_classes.Room("Home")
    room_1 = main_classes.Room("Parking lot", item_collection[0])
    room_2 = main_classes.Room("Alley", item_collection[1])
    room_3 = main_classes.Room("Football field", item_collection[2])
    room_4 = main_classes.Room("Playground", item_collection[3])
    room_5 = main_classes.Room("Public park", item_collection[4])
    room_6 = main_classes.Room("Bus stop", item_collection[5])
    room_7 = main_classes.Room("Train station", item_collection[6])
    room_8 = main_classes.Room("Subway tunnel", item_collection[7])
    room_9 = main_classes.Room("Old warehouse", item_collection[8])
    room_10 = main_classes.Room("Junkyard", item_collection[9])
    room_11 = main_classes.Room("Construction site", item_collection[10])
    room_12 = main_classes.Room("Gas station", item_collection[11])
    room_13 = main_classes.Room("Supermarket", item_collection[12])
    room_14 = main_classes.Room("Shopping mall", item_collection[13])
    room_15 = main_classes.Room("Mall rooftop", item_collection[14])
    return [room_0,room_1,room_2,room_3,room_4,room_5,room_6,room_7,room_8,room_9,room_10,room_11,room_12,room_13,room_14,room_15]

# Creates a player object if there is no player object (Controlling creation of player object if it already exists from load)
def player_creator(player,user_name,room_list):
    if player == None:
        return main_classes.Player(user_name,room_list[0])

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
    

# This code contains the internal part of the game which starts when the game is started from the Main Menu
def start_game(player,user_name,user_age,room_list):

    def movement_inp():
            print(f"\nYou are currently at {player.location.name}.\n\nEnter W to move to the next location\nEnter E to end game")
            user_mov_raw = str(input("\nEnter command: "))
            user_mov_com = user_mov_raw.lower()
            return user_mov_com
    
    def item_dealing():
        print(f"\nEntering {player.location.name}..")
        time.sleep(1)
        print(f"You entered {player.location.name}!")
        time.sleep(1)
        print(f"\nYou have encountered an item!")
        time.sleep(1)
        print(f"\nAnalyzing the item....")
        time.sleep(2)
        print(f"Hint: {player.location.item.riddle}")
        print(f"Weight of the item is {player.location.item.weight}")
        time.sleep(5)
        user_decision_raw = str(input("\nEnter T to throw it in the dustbin\tEnter R to report it to the police!\n"))
        user_decision_com = user_decision_raw.lower()
        return user_decision_com
    
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

    for n in room_list:
        if n.name == player.location.name:
            i = room_list.index(n)

    while i >= 0 and i < 14:
        if user_mov == "w":
            player.location = room_list[i+1]

            while item_dealt == False:
                user_decision = item_dealing()

                if user_decision == "t":
                    item_dealt = True

                    if player.location.item.trash == True:
                        print("\nYou have guessed right! You get Citizen points.")
                        player.citizen_points += ( 5 * i)
                        time.sleep(1)
                        print(f"\nCurrent Citizen life: {player.citizen_life}")
                        print(f"Current Citizen points: {player.citizen_points}")
                        time.sleep(2)
                    else:
                        print(f"\nYou threw someone's {player.location.item.name} in the trash and now they might never find it! Citizen life deducted!")
                        player.citizen_life -= (5 * i)
                        time.sleep(1)
                        print(f"\nCurrent Citizen life: {player.citizen_life}")
                        print(f"Current Citizen points: {player.citizen_points}")
                        time.sleep(2)

                elif user_decision == "r":
                    item_dealt = True

                    if player.location.item.trash == False:
                        print("\nYou have guessed right! You get Citizen points.")
                        player.citizen_points += ( 5 * i)
                        time.sleep(1)
                        print(f"\nCurrent Citizen life: {player.citizen_life}")
                        print(f"Current Citizen points: {player.citizen_points}")
                        time.sleep(2)
                    else:
                        print(f"\nPolice officer: Why did you bring {player.location.item.name} here?! Citizen life deducted!")
                        player.citizen_life -= (5 * i)
                        time.sleep(1)
                        print(f"\nCurrent Citizen life: {player.citizen_life}")
                        print(f"Current Citizen points: {player.citizen_points}")
                        time.sleep(2)
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
    

    