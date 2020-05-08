# Implement a class to hold room information. This should have name and description attributes.

class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.items = []
    
    def __str__(self):
        return f"{self.name}: {self.description}"
    
    def player_grabs_item(self, item):
        return self.items.remove(item)

    def player_drops_item(self, item):
        return self.items.append(item)