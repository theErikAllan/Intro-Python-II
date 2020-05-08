from room import Room
from player import Player
from item import Item

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance", """North of you, the cave mount beckons"""),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling into the darkness. Ahead to the north, a light flickers in the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure chamber! Sadly, it has already been completely emptied by earlier adventurers. The only exit is to the south."""),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

# List items

all_items = {
    "rock": Item("rock", "a stone eroded and smoothed by time"),
    "notebook": Item("notebook", "a collection of scribbled journal entries"),
    "pen": Item("pen", "weapon of choice for movers of nations"),
    "candle": Item("candle", "tamer of the flame and creator of dancing shadows"),
    "bone": Item("bone", "the last remnant of a life you'll never know"),
    "feather": Item("feather", "why is this here"),
}

room['outside'].items.append(all_items["rock"])
room['foyer'].items.append(all_items["notebook"])
room['foyer'].items.append(all_items["pen"])
room['overlook'].items.append(all_items["candle"])
room['narrow'].items.append(all_items["bone"])
room['narrow'].items.append(all_items["feather"])

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
player = Player("Harry", room['outside'])



# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#cl
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

# can add a condition such as while game_running = true
# idea - create table of commands, with each command linked to a function
while True:
    print("\n")
    print(player.current_room.name)
    print(player.current_room.description)
    print("\n")
    print(f"Items in {player.current_room.name}:" )
    for item in player.current_room.items:
        print(item)
    print("\n")
    action = input("Please enter a command: ").lower().split(" ")
    print("\n")
    # print(player.current_room.__dict__)
    # Add option to quit
    if len(action) == 1:
        if action[0] in ("n", "s", "e", "w"):
            if hasattr(player.current_room,f'{action[0]}_to'):
                player.current_room = getattr(player.current_room, f'{action[0]}_to')
            else:
                print("You cannot move in that direction, please choose another direction ")
                continue
        if action[0] in ("i", "inventory"):
            print("You're holding: ")
            for item in player.inventory:
                print(item)
        if action[0] in ("q", "quit", "exit"):
            exit()
    elif len(action) == 2 and action[0] in ['grab', 'take']:
        current_room_items = [item.name for item in player.current_room.items]
        if action[1] in current_room_items:
            player.grab_item(all_items[action[1]])
            player.current_room.player_grabs_item(all_items[action[1]])
            print("You're holding: ")
            for item in player.inventory:
                print(item)
        else:
            print("That item isn't present")
    elif len(action) == 2 and action[0] == 'drop':
        current_inventory = [item.name for item in player.inventory]
        if action[1] in current_inventory:
            player.drop_item(all_items[action[1]])
            player.current_room.player_drops_item(all_items[action[1]])
            print("You're holding: ")
            for item in player.inventory:
                print(item)

            



# done = False

# def move_to(direction, current_loc):
#     # try to move in the specified direction
#     attribute = direction + '_to'

#     #if we can move in specified direction from our current location
#     if hasattr(current_loc, attribute):
#         #get the room in the specified direction
#         return getattr(current_loc, attribute)

# while not done:
#     print(player.current_room)

#     for line in textwrap.wrap(player.current_room.print_description()):
#         print(line)

#     command = input("What do you want to do? ")

#     if command in ['n', 's', 'e', 'w']:
#         player.location = move_to(command, player.current_room)

#     if command == 'q' or command == 'quit':
#         done = True
