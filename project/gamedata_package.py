import main_classes
import json
from pathcreator_package import path_creator

# Saves user data in dictionary form and uses a nested dictionary created from method of player class to save the required data for continuation. 
def game_save(user_name,user_age,player):
    player_data = {
        "user_name": user_name,
        "user_age": user_age,
        "player": player.save_player()
    }

    filename = f"save_{user_name}.json"
    path = path_creator(filename)    
    with open(path, "w") as file:
        json.dump(player_data, file)

# Loads the data of a player if the user of that player comes back and their name and age matches.
# Uses the player key and retrieves the internal dictionary which has properties of the saved player object
# Uses the values of the internal dictionary and returns the recreated player object
def game_load(user_name, user_age):
    try:
        filename = f"save_{user_name}.json"
        path = path_creator(filename)
        with open(path, "r") as file:
            player_data = json.load(file)
            
    except FileNotFoundError:
        print("\nNo saved game found!")
        return
    
    if user_name == player_data["user_name"] and user_age == player_data["user_age"]:
        p = player_data["player"]

        location = main_classes.Room(p["location"])

        return main_classes.Player(p["name"], location, p["citizen_life"], p["citizen_points"])

    else:
        print("\nNo saved game with your name and age!")
        return None

