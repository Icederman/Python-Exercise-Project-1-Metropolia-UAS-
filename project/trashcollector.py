import time 
import json

minor_border = 12
game_loaded = False
player = None

menu_input = ""
powerup_inventory = []
inventory_limit = 2
trashbag = []


class Player():
    def __init__(self,name,bag,location):
        self.name = name
        self.bag = bag
        self.location = location

    def save_player(self):
        bg = []
        for i in self.bag:
            bg.append({"name": i.name, "weight": i.weight})

        return {"name":self.name, "bag":bg, "location":self.location.name}

class Room():
    def __init__(self,name,item=""):
        self.name = name
        self.item = item

class Item():
    def __init__(self,name,weight):
        self.name = name
        self.weight = weight

def show_intro(filename):
    try:
        with open(filename, "r") as file:
            print(f"\n{file.read()}")
    except FileNotFoundError:
        print("File not found!")

def show_rules(filename):
    try:
        with open(filename, "r") as file:
            print(f"\n{file.read()}")
    except FileNotFoundError:
        print("File not found!")        

def pre_game():
    print("\nEnter N to start new game\nEnter L to load game from last save\nEnter E to exit")
    user_pre_raw = str(input("\nEnter command: "))
    user_pre_com = user_pre_raw.lower()
    return user_pre_com

def game_load():
    global player, user_name, user_age, game_loaded
    try:
        filename = f"save_{user_name}.json"
        with open(filename, "r") as file:
            player_data = json.load(file)
            
    except FileNotFoundError:
        print("\nNo saved game found!")
        return
    
    if user_name == player_data["user_name"] and user_age == player_data["user_age"]:
        p = player_data["player"]
        bag = []
        for i in p["bag"]:
            bag.append(Item(i["name"], i["weight"]))

        location = Room(p["location"])

        player = Player(p["name"], bag, location)

        game_loaded = True

    else:
        print("\nNo saved game with your name and age!")



def game_save(player):
    player_data = {
        "user_name": user_name,
        "user_age": user_age,
        "player": player.save_player()
    }

    filename = f"save_{user_name}.json"
    with open(filename, "w") as file:
        json.dump(player_data, file)

def start_game():
    global player
    print("\nLoading Game...")
    time.sleep(2)
    print("\nLoading..")
    time.sleep(1)
    print("\nLoading.")
    time.sleep(1)
    print("\nGame Started!")
    time.sleep(1)

    item_1 = Item("Banana peel", 30)
    item_2 = Item("Candy wrapper", 5)
    item_3 = Item("Wallet", 200)

    item_coll = [item_1,item_2,item_3]

    room_0 = Room("Home")
    room_1 = Room("Parking lot", item_1)
    room_2 = Room("Alley", item_2)
    room_3 = Room("Football field", item_3)

    item_rooms = [room_1,room_2,room_3]

    if player == None:
        player = Player(user_name, trashbag, room_0)


    def movement_inp():
        print(f"\nYou are currently at {player.location.name}.\n\nEnter W to move to the next location\nEnter E to end game")
        user_mov_raw = str(input("\nEnter command: "))
        user_mov_com = user_mov_raw.lower()
        return user_mov_com

    def pickup_input():
        print(f"\nEntering {player.location.name}..")
        time.sleep(1)
        print(f"You entered {player.location.name}!")
        time.sleep(1)
        print(f"\nYou have encountered an item!\nEnter P to pick it up!")
        user_pick_raw = str(input("\nEnter command: "))
        user_pick_com = user_pick_raw.lower()
        return user_pick_com
        

    user_mov = movement_inp()
    i=0

    while i >= 0 and i <= 2:
        if user_mov == "w":
            player.location = item_rooms[i]
            user_pick = pickup_input()

            if user_pick == "p":
                player.item = item_coll[i]
                print(f"\nYou have picked the item!")
                player.bag.append(player.item)
                i+=1
                time.sleep(2)
                if i != 3:
                    user_mov = movement_inp()
                else:
                    print("\nDone!")
                    #More code upcoming!
            else:
                print("\nInvalid command!")
                time.sleep(1)

        elif user_mov == "e":
            print("\nReturning to Main Menu!")
            break
        else:
            print("\nInvalid Command! Try Again!")
            time.sleep(1)
            user_mov = movement_inp()    
    
    
def powerup_chooser():

    while len(powerup_inventory) < inventory_limit:
        print("\nChoose your powerups:\n\nHappiness\tLife\tSkipItem\tLuck")
        powerup_inp = str(input("\nEnter the powerup you want: "))
        powerup = powerup_inp.lower()
        if powerup == "happiness" or powerup == "life" or powerup == "skipitem" or powerup ==  "luck":
            print("\nPutting chosen powerup in your inventory..\n")
            time.sleep(1)
            powerup_inventory.append(powerup)
        else:
            print("\nNot available! Choose again!\n")
            time.sleep(1)

    if len(powerup_inventory) == 2:
        print("Inventory full!")
            


def show_inventory():
    print("\nPowerups:")
    for i in powerup_inventory:
        print(f"\t{i}")
    if(len(powerup_inventory) == 0):
        print("\nYou have not chosen the powerups yet!")

def show_powerups():
    for n in powerup_inventory:
        print(n)


def name_change():
    global user_name
    user_name = str(input("\nEnter Your Name: "))
    print(f"\nName has been changed to {user_name}! Returning to Main Menu..")

def show_credits():
    time.sleep(1)
    print("\nProject creator: Safwan MD Solaiman")
    print("\nReturning to Main Menu..")

def exit_app():
    print("\nExiting Game!\n")
    time.sleep(2)

def invalid_com():
    print("\nCommand is not valid! Returning to Main Menu..")

show_intro("intro.txt")
time.sleep(3)
show_rules("rules.txt")
time.sleep(15)
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
                    start_game()

                elif user_pre == "l":
                    game_load()

                    if player == None:
                        command_started = False
                        time.sleep(1)
                        user_pre = pre_game()

                    else:
                        command_started = True
                        print("Continuing from previous save..")
                        time.sleep(1)
                        start_game()

                elif user_pre == "e":
                    command_started = True
                    exit_app()

                else:
                    print("\nInvalid Command! Try Again!")
                    time.sleep(1)
                    user_pre = pre_game()

        elif menu_input == "p":
            powerup_chooser()

        elif menu_input == "i":
            show_inventory()
                
        elif menu_input == "n":
            name_change()

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
                        game_save(player)
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

        
        