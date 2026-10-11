import time

# Pre-game function which asks the user if they want to start a new game, load previous game or exit
def pre_game():
    print("\nEnter N to start new game\nEnter L to load game from last save or to see your previous score\nEnter E to exit")
    user_pre_raw = str(input("\nEnter command: "))
    user_pre_com = user_pre_raw.lower()
    return user_pre_com

# This function is built for the user to choose two unique powerups from the option of 3!
def powerup_chooser(powerup_inventory,inventory_limit):

    while len(powerup_inventory) < inventory_limit:
        print("\nChoose your powerups:\n\nReveal\tLife\tSkip")
        powerup_inp = str(input("\nEnter the powerup you want: "))
        powerup = powerup_inp.lower()
        if powerup == "reveal" or powerup == "life" or powerup == "skip":
            if powerup in powerup_inventory:
                print("\nYou cannot choose this anymore! Choose another one instead.")
                time.sleep(1)
            else:
                print("\nPutting chosen powerup in your inventory..\n")
                powerup_inventory.append(powerup)
                time.sleep(1)
        else:
            print("\nInvalid! Try again.")
            time.sleep(1)
    if len(powerup_inventory) == 2:
        print("Inventory full!")

# This function displays the powerups
def show_inventory(powerup_inventory):
    print("\nPowerups:")
    for i in powerup_inventory:
        print(f"\t{i}")
    if(len(powerup_inventory) == 0):
        print("\nYou have not chosen the powerups yet!")

# Returns the changed name for the user
def name_change():
    changed_name = str(input("\nEnter Your Name: "))
    print(f"\nName has been changed to {changed_name}! Returning to Main Menu..")
    return changed_name

# This function displays credits
def show_credits():
    time.sleep(1)
    print("\nProject creator: Safwan MD Solaiman")
    print("\nReturning to Main Menu..")

# Function used to display exit message
def exit_app():
    print("\nExiting Game!\n")
    time.sleep(2)

# Function used for showing invalid command in Main Menu
def invalid_com():
    print("\nCommand is not valid! Returning to Main Menu..")