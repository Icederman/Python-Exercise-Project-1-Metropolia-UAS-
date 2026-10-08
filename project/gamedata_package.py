import main_classes
import json

# Saves data in dictionary form and uses a nested dictionary to save properties of player object
def game_save(user_name,user_age,player):
    player_data = {
        "user_name": user_name,
        "user_age": user_age,
        "player": player.save_player()
    }

    filename = f"save_{user_name}.json"
    with open(filename, "w") as file:
        json.dump(player_data, file)

# Loads the data of a player if the user of that player comes back and their name and age matches.
# Uses the player key and converts the values of the nested dictionary to objects to use them as properties for the new player object which is identical to the intended saved Player object.
def game_load(user_name, user_age):
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
            bag.append(main_classes.Item(i["name"], i["weight"]))

        location = main_classes.Room(p["location"])

        return main_classes.Player(p["name"], bag, location)

    else:
        print("\nNo saved game with your name and age!")
        return None

