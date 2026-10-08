import time
import main_classes


# Creates the items meant for the rooms and returns a list of those items
def item_list_creator():

    item_1 = main_classes.Item("Banana peel", 30)
    item_2 = main_classes.Item("Candy wrapper", 5)
    item_3 = main_classes.Item("Wallet", 200)

    return [item_1,item_2,item_3]

# Creates rooms of the game and returns the list of those rooms
def room_list_creator(item_collection):
    room_0 = main_classes.Room("Home")
    room_1 = main_classes.Room("Parking lot", item_collection[0])
    room_2 = main_classes.Room("Alley", item_collection[1])
    room_3 = main_classes.Room("Football field", item_collection[2])

    return [room_0,room_1,room_2,room_3]

# Creates a player object if there is no player object (Controlling creation of player object if it already exists from load)
def player_creator(player,user_name,trashbag,room_list):
    if player == None:
        return main_classes.Player(user_name, trashbag, room_list[0])

# Main logic behind the game
def start_game(player,item_collection,room_list):

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

    print("\nLoading Game...")
    time.sleep(2)
    print("\nLoading..")
    time.sleep(1)
    print("\nLoading.")
    time.sleep(1)
    print("\nGame Started!")
    time.sleep(1)


    user_mov = movement_inp()

    i = 0

    for n in room_list:
        if n.name == player.location.name:
            i = room_list.index(n)

    while i >= 0 and i <= 2:
        if user_mov == "w":
            player.location = room_list[i+1]
            user_pick = pickup_input()

            if user_pick == "p":
                player.item = item_collection[i]
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

    