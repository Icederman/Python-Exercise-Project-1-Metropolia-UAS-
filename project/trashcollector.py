import time #Experience from Unity(C#)

user_name = str(input("\nEnter Your Name: "))
user_age = int(input("Enter Your Age: "))
menu_input = ""

print(f"\nName: {user_name}")
print(f"Age: {user_age}")


if user_age < 12:
    print("\nYou are a minor and this game is not for minors! Exiting application..")
    time.sleep(2)

else:
    print(f"\nWelcome {user_name}! Loading Main Menu...")
    while menu_input != "lopeta":
        time.sleep(2)
        print("\nMain Menu\n\nEnter S to Start\n\nEnter N to change name\n\nEnter C for Credits\n\nEnter lopeta to exit")
        menu_input_raw = str(input("\nEnter command: "))
        menu_input = menu_input_raw.lower()

        if menu_input == "s":
            print("\nLoading Game...")
            time.sleep(2)
            print("\nLoading..")
            time.sleep(1)
            print("\nLoading.")
            time.sleep(1)
            print("\nGame Started!")
            # More code coming up
            time.sleep(1)
            print("\nGame will be available soon! Returning to Main Menu..")

        elif menu_input == "n":
            user_name = str(input("\nEnter Your Name: "))
            print(f"\nName has been changed to {user_name}! Returning to Main Menu..")

        elif menu_input == "c":
            print("\nProject creator: Safwan MD Solaiman")
            print("\nReturning to Main Menu..")

        elif menu_input == "lopeta":
            print("\nExiting Game!\n")
            time.sleep(2)

        else:
            print("\nCommand is not valid! Returning to Main Menu..")

        
        