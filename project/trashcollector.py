import time #Experience from Unity(C#)

user_name = str(input("\nEnter Your Name: "))
user_age = int(input("Enter Your Age: "))
minor_border = 12

menu_input = ""
powerup_inventory = []
inventory_limit = 2
trashbag = []

print(f"\nName: {user_name}")
print(f"Age: {user_age}")

class Player():
    def __init__(self,name,bag,location):
        self.name = name
        self.bag = bag
        self.location = location

class Room():
    def __init__(self,name,item=""):
        self.name = name
        self.item = item

class Item():
    def __init__(self,name,weight):
        self.name = name
        self.weight = weight
        

def start_game():
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

    

if user_age < minor_border:
    print("\nYou are a minor and this game is not for minors! Exiting application..")
    time.sleep(2)

else:
    print(f"\nWelcome {user_name}! Loading Main Menu...")
    while menu_input != "lopeta":
        time.sleep(2)
        print("\nMain Menu\n\nEnter S to Start\n\nEnter P to choose your powerups\n\nEnter I to show Powerup Inventory\n\nEnter N to change name\n\nEnter C for Credits\n\nEnter lopeta to exit")
        menu_input_raw = str(input("\nEnter command: "))
        menu_input = menu_input_raw.lower()
    
        if menu_input == "s":
            start_game()

        elif menu_input == "p":
            powerup_chooser()

        elif menu_input == "i":
            show_inventory()
                
        elif menu_input == "n":
            name_change()
                
        elif menu_input == "c":
            show_credits()

        elif menu_input == "lopeta":
            exit_app()

        else:
            invalid_com()

        
        