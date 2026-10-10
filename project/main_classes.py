class Player():
    def __init__(self,name,location,citizen_life = 100,citizen_points=0):
        self.name = name
        self.location = location
        self.citizen_life = citizen_life
        self.citizen_points = citizen_points

    # This method returns a dictionary where the properties are the values which can be called by their relevant keys. 
    # It is creating a list of dictionaries for bag property as it holds items with multiple properties so that when we load the game we can retrieve the values in order to recreate the identical class.
    def save_player(self):
        return {"name":self.name, "location":self.location.name, "citizen_life": self.citizen_life, "citizen_points": self.citizen_points}

class Room():
    def __init__(self,name,item=""):
        self.name = name
        self.item = item

class Item():
    def __init__(self,name,riddle,weight,trash = True):
        self.name = name
        self.riddle = riddle
        self.weight = weight
        self.trash = trash