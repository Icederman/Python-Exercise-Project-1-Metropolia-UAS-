import time

def pre_game():
    print("\nEnter N to start new game\nEnter L to load game from last save or to see your previous score\nEnter E to exit")
    user_pre_raw = str(input("\nEnter command: "))
    user_pre_com = user_pre_raw.lower()
    return user_pre_com

def powerup_chooser(powerup_inventory,inventory_limit):

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
            


def show_inventory(powerup_inventory):
    print("\nPowerups:")
    for i in powerup_inventory:
        print(f"\t{i}")
    if(len(powerup_inventory) == 0):
        print("\nYou have not chosen the powerups yet!")

def name_change():
    changed_name = str(input("\nEnter Your Name: "))
    print(f"\nName has been changed to {changed_name}! Returning to Main Menu..")
    return changed_name

def show_credits():
    time.sleep(1)
    print("\nProject creator: Safwan MD Solaiman")
    print("\nReturning to Main Menu..")

def exit_app():
    print("\nExiting Game!\n")
    time.sleep(2)

def invalid_com():
    print("\nCommand is not valid! Returning to Main Menu..")