# You are creating an "Escape the room" game. 
# The first step is to create a hash table ( dict in Python) called rooms that contains all of the rooms of the game. 
# There should be at least 3 rooms inside it, each room being a hash table with at least 3 properties (e.g. name, description, completed).

rooms = {
    "hall": {
        "name": "Hall",
        "description": "A grand hall with a large staircase.",
        "exits": {"north": "kitchen", "east": "dining_room"}
    },
    "kitchen": {
        "name": "Kitchen",
        "description": "A modern kitchen with a large island.",
        "exits": {"south": "hall"}
    },
    "dining_room": {
        "name": "Dining Room",
        "description": "An elegant dining room with a long table.",
        "exits": {"west": "hall"}
    }


  # rooms = { "Room_1":{"Guest_Name":"Hardik","Room_Number":"69","Hotel":"Royal Inn"},
  #         "Room_2":{"Guest_Name":"Hridhik","Room_Number":"369","Hotel":"Sandesh The Prince"},
  #         "Room_3":{"Guest_Name":"Pratham","Room_Number":"96","Hotel":"The Quorum"},
  #         "Room_4":{"Guest_Name":"Ruturaj","Room_Number":"14","Hotel":"Radisson Blu"}}


  # rooms = {'room1': {'name': 'name1', 'description': 'description1', 'completed': 'no'},
  #        'room2': {'name': 'name2', 'description': 'description2', 'completed': 'no'},
  #        'room3': {'name': 'name3', 'description': 'description3', 'completed': 'no'}
  #        }
