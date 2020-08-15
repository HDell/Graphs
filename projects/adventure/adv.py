from room import Room
from player import Player
from world import World

import random
from ast import literal_eval

import os
dirpath = os.path.dirname(os.path.abspath(__file__))
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

class RoomGraph():

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

    def dft(self, starting_room_id, graph):
        """
        Traverse through all rooms from a given a starting room, depth first.
        """
        # picks a random unexplored direction
        visited = set()
        current_room = starting_room_id
        start = Stack()
        reverse = Stack()
        path = []
        all_visited = True
        exit_direction_list = list(self.get_neighbors(current_room).keys())
        for direction in exit_direction_list:
            if self.get_neighbors(current_room)[direction] == '?':
                all_visited = False
                start.push(direction)
                if direction == 'n':
                    reverse.push('s')
                elif direction == 's':
                    reverse.push('n')
                elif direction == 'w':
                    reverse.push('e')
                else: # direction == 'e'
                    reverse.push('w')
                visited.add(current_room)

        while start.size() > 0:
            print(len(path), ":", current_room)
            if all_visited:
                next_direction = reverse.pop() #n
                path.append(next_direction) #n
                if len(path) == 561:
                    print("debug")
                try_again = True
                while try_again:
                    try:
                        next_room = graph[current_room][1][next_direction] # next_room = room number (id)
                        try_again = False
                    except:
                        next_direction = reverse.pop()
                        if next_direction is not None:
                            try_again = True
                current_room = next_room
                exit_direction_list = list(self.get_neighbors(current_room).keys()) #['n', 's']
                for direction in exit_direction_list:
                    if self.get_neighbors(current_room)[direction] == '?':
                        if current_room in visited:
                            all_visited = False
                            break
                        else:
                            all_visited = False
                            start.push(direction)
                            if direction == 'n':
                                reverse.push('s')
                            elif direction == 's':
                                reverse.push('n')
                            elif direction == 'w':
                                reverse.push('e')
                            else: # direction == 'e'
                                reverse.push('w')
            else:
                next_direction = start.pop() #s
                if next_direction == 'n':
                    reverse_direction = 's'
                elif next_direction == 's':
                    reverse_direction = 'n' #this -> n
                elif next_direction == 'w':
                    reverse_direction = 'e'
                else: # next_direction == 'e'
                    reverse_direction = 'w'
                next_room = graph[current_room][1][next_direction] # next_room = room number (id)
                if self.rooms[current_room][next_direction] == '?' or self.rooms[next_room][reverse_direction] == '?':
                    try:
                        graph[next_room][1][reverse_direction]
                        path.append(next_direction)
                        self.rooms[current_room][next_direction] = next_room 
                        self.rooms[next_room][reverse_direction] = current_room
                        current_room = next_room
                    except:
                        self.rooms[current_room][next_direction] = next_room
                        reverse.pop() 
                else:
                    continue
                if current_room in visited and len(self.get_neighbors(current_room).keys())==4:
                    while reverse.size() > start.size():
                        reverse.pop()
                    continue
                visited.add(current_room)
                all_visited = True
                exit_direction_list = list(self.get_neighbors(current_room).keys()) #[n]
                for direction in exit_direction_list: #n
                    if self.get_neighbors(current_room)[direction] == '?': 
                        all_visited = False
                        start.push(direction)
                        if direction == 'n':
                            reverse.push('s')
                        elif direction == 's':
                            reverse.push('n')
                        elif direction == 'w':
                            reverse.push('e')
                        else: # direction == 'e'
                            reverse.push('w')
        return path

        # travels
        # logs that direction
        # loops


"""
"""
# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = dirpath + "/maps/test_line.txt"
# map_file = dirpath + "/maps/test_cross.txt"
# map_file = dirpath + "/maps/test_loop.txt"
# map_file = dirpath + "/maps/test_loop_fork.txt"
map_file = dirpath + "/maps/main_maze.txt"

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
for room in room_graph:
    graph.add_room(room, list(room_graph[room][1].keys()))

# print("Class:", graph.rooms)
# print("Neighbors:", graph.get_neighbors(0))
# print("DFT:", graph.dft(player.current_room.id, room_graph))
traversal_path = graph.dft(player.current_room.id, room_graph)

# TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

# print("Room:::", player.current_room.id)
# print("Exit:::", player.current_room.get_exits())
# print("Graph:::", room_graph) 
#room_graph[player.current_room.id][1]['n'] in visited
#room_graph[player.current_room.id][1]['s'] in visited
#room_graph[player.current_room.id][1]['e'] in visited
#room_graph[player.current_room.id][1]['w'] in visited
print("Length:::", len(room_graph))
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
