import time #Experience from Unity(C#)

user_name = str(input("\nEnter Your Name: "))
user_age = int(input("Enter Your Age: "))
minor_border = 12

menu_input = ""
powerup_inventory = []
inventory_limit = 2

print(f"\nName: {user_name}")
print(f"Age: {user_age}")

def start_game():
    print("\nLoading Game...")
    time.sleep(2)
    print("\nLoading..")
    time.sleep(1)
    print("\nLoading.")
    time.sleep(1)
    print("\nGame Started!")
    time.sleep(1)
    print("\nGame under construction! Returning to Main Menu..")
    
    
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
    print("\nInventory:")
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
        print("\nMain Menu\n\nEnter S to Start\n\nEnter P to choose your powerups\n\nEnter I to show Inventory\n\nEnter N to change name\n\nEnter C for Credits\n\nEnter lopeta to exit")
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

        
        