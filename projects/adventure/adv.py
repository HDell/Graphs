from room import Room
from player import Player
from world import World

import random
from ast import literal_eval
"""
Graph, Stack, and Queue Classes
"""

class Queue():
    def __init__(self):
        self.queue = []
    def enqueue(self, value):
        self.queue.append(value)
    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None
    def size(self):
        return len(self.queue)

class Stack():
    def __init__(self):
        self.stack = []
    def push(self, value):
        self.stack.append(value)
    def pop(self):
        if self.size() > 0:
            return self.stack.pop()
        else:
            return None
    def size(self):
        return len(self.stack)

class RoomGraph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.rooms = {}

    def add_room(self, room_id, exits): #int, list
        """
        Add a room to the graph along with its exits.
        """
        if room_id not in self.rooms:
            self.rooms[room_id] = {}
            for r_exit in exits:
                self.rooms[room_id][r_exit] = '?'
            return True
        else:
            return False


    def add_exit_id(self, room1, direction, room2):
        """
        Add a directed edge to the graph.
        """
        if room1 == room2:
            return False
        else:
            reverse_direction = ''
            if direction == 'n':
                reverse_direction = 's'
            elif direction == 's':
                reverse_direction = 'n'
            elif direction == 'w':
                reverse_direction = 'e'
            else: # direction == 'e'
                reverse_direction = 'w'
            self.rooms[room1][direction] = room2
            self.rooms[room2][reverse_direction] = room1
            return True

    def get_neighbors(self, room_id):
        """
        Get all adjacent rooms to a given room.
        """
        return self.rooms[room_id] # e.g. {'n': ?, 's': ?}

    def dft(self, starting_room_id):
        """
        Traverse through all rooms from a given a starting room, depth first.
        """
        visited = set()
        # picks a random unexplored direction
        exit_direction_list = self.get_neighbors(starting_room_id)
        stack = Stack()
        next_direction = ''
        for direction in exit_direction_list:
            if exit_direction_list[direction] == '?':
                next_direction = direction
                break
        stack.push([next_direction])
        while stack.size() > 0:
            current_path = stack.pop()
            last_direction = current_path[-1]
            player.travel(last_direction)
            last_room = player.current_room.id
            if last_room not in visited:
                visited.add(last_room)
            for direction in player.current_room.get_exits():
                path_copy = list(current_path)
                path_copy.append(direction)
                stack.push(path_copy)
        return current_path

        # travels
        # logs that direction
        # loops


"""
"""
# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
# map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = []
graph = RoomGraph()



# TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

print("Room:::", player.current_room.id)
print("Exit:::", player.current_room.get_exits())
if len(visited_rooms) == len(room_graph):
    print(f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")



#######
# UNCOMMENT TO WALK AROUND
#######
# player.current_room.print_room_description(player)
# while True:
#     cmds = input("-> ").lower().split(" ")
#     if cmds[0] in ["n", "s", "e", "w"]:
#         player.travel(cmds[0], True)
#     elif cmds[0] == "q":
#         break
#     else:
#         print("I did not understand that command.")
