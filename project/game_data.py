import main_classes
import json
from path_creator import path_creator

# Saves user data in dictionary form created from method of player class to save the required data for continuation in json format. 
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
# Returns a new Player object with similar properties after retrieving the values so that we can assign it to a player variable and work with that during the game.
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

        return main_classes.Player(p["name"], p["location"], p["powerup_inventory"], p["area"], p["citizen_life"], p["citizen_points"])

    else:
        print("\nNo saved game with your name and age!")
        return None

