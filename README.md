# Global Citizen
Project Creator- Safwan MD Solaiman

# Game Idea & Objective-
The main character of this game is a common citizen of a country which is controlled by the player. The player's main objective is to become the **Ultimate Global Citizen**. At the beginning of the game the player gets to select their route which is basically selecting a map. Each of the routes have different areas where the player goes one by one and encounters an item. The player gets a hint which is technically a riddle for the player to solve and decide whether they want to throw the item in the dustbin or report it to the police station. Correct choices give the player Citizen points and incorrect choices deduct Citizen points from the player. To become the 'Ultimate Global Citizen', the player must survive till the last area.

Players can choose 2 powerups each session.

Some players would not be able to finish the game but they would have a final score to keep with them and compare with their peers!

# Functionality- 
The player has to type the required keyword to move forward with a decision. The Main Menu asks the player to write whatever function the player wants to use. When the player is in the Main Menu and Game Menu, the player would have to enter single letters and sometimes full words to proceed according to the situation. For example, moving to another area requires the player to press w, choosing or using a powerup requires the player to enter the whole word etc.



# Relation with SDG
The player solves riddles and decides to throw trash in the dustbin and report personal belongings of other people to the police while having the goal to become the **Ultimate Global Citizen**.
So, when a player throws trash in the correct place and reports belongings to the police it promotes the **11th SDG "Sustainable Cities and Communities"**. Moreover, throwing trash into proper place reduces pollution which promotes good health, life on land and life below water which are the 3rd, 13th, 14th and 15th SDG.


# Structure of the project
8 Relevant Modules 

menu_funcs - Contains functions relevant to the Main Menu
game_manager- Contains core functions which start and end the main part of the game
class_powerup_handler - Contains functions used for creation of objects and functions related to powerup selection of the user
game_data - Contains functions which handle data persistency and data between sessions
path_creator - Contains a function which joins path of the current running file with the file we need to work with (Reading,Writing etc)
text_reader - Contains a function which is used to read files

main_classes - Contains definition for the main game classes

globalcitizen - Main module which calls the functions, operates the whole project (Main aspect is function calling from different modules and also has a big role in handling Main Menu inputs)

# Pre-requisites

- **Python 3.10 or newer** (this project was developed with Python 3.14)
- A terminal (Command Prompt, Powershell, macOS Terminal,or a Linux Shell)

For Windows -

1. Go to the official download page: https://www.python.org/downloads/
2. Click **Download Python** to get the latest installer.
3. Run the installer.
4. **Tick "Add python.exe to PATH"** at the bottom of the first screen.
5. Click **Install Now** and wait for it to finish.
6. Open a new Command Prompt or PowerShell window and check the install:
    python --version

For macOS - 

1. Go to https://www.python.org/downloads/macos/ and download the latest installer.
2. Open the `.pkg` file and follow the steps.
3. Open Terminal and check the install:
    python3 --version

For Linux-

1. Open a terminal and run:

   sudo apt update
   sudo apt install python3 python3-pip

2. Check the install:
   python3 --version


