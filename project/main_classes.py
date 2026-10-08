class Player():
    def __init__(self,name,bag,location):
        self.name = name
        self.bag = bag
        self.location = location

    def save_player(self):
        bg = []
        for i in self.bag:
            bg.append({"name": i.name, "weight": i.weight})

        return {"name":self.name, "bag":bg, "location":self.location.name}

class Room():
    def __init__(self,name,item=""):
        self.name = name
        self.item = item

class Item():
    def __init__(self,name,weight):
        self.name = name
        self.weight = weight