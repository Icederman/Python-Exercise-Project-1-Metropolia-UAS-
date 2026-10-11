# Main player class
class Player():
    def __init__(self,name,location,powerup_inventory,area,powerup_taken,citizen_life = 100,citizen_points=0):
        self.name = name
        self.location = location
        self.powerup_inventory = powerup_inventory
        self.area = area
        self.powerup_taken = powerup_taken
        self.citizen_life = citizen_life
        self.citizen_points = citizen_points
        
    # This method returns a dictionary where the properties are the values which can be called by their relevant keys so that we can save it as json file for loading again.
    # Powerup inventory is a list, so it also saves a list under it!
    def save_player(self):
        return {
            "name":self.name, "location":self.location.name,
            "powerup_inventory": self.powerup_inventory, 
            "area": self.area,
            "powerup_taken":self.powerup_taken,
            "citizen_life": self.citizen_life, 
            "citizen_points": self.citizen_points
            }
    
# Area class
class Area():
    def __init__(self,name,item=""):
        self.name = name
        self.item = item

# Item class
class Item():
    def __init__(self,name,riddle,weight,trash = True):
        self.name = name
        self.riddle = riddle
        self.weight = weight
        self.trash = trash