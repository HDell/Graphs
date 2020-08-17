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
    def peek(self):
        if self.size() > 0:
            return self.stack[len(self.stack) - 1]
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

    def dft(self, starting_room_id, graph, player):
        """
        Traverse through all rooms from a given a starting room, depth first.
        """
        # picks a random unexplored direction
        # picks a random unexplored direction
        visited = {}
        backward = Stack()
        path = []
        visited[player.current_room.id] = player.current_room.get_exits()
        while len(visited) < len(graph):
            if len(visited) == 11:
                print("start")
            if player.current_room.id not in visited.keys():
                visited[player.current_room.id] = player.current_room.get_exits()
                visited[player.current_room.id].remove(backward.peek())
                if len(visited) == len(graph):
                    return path

            try:
                next_direction = visited[player.current_room.id].pop()
                reverse_direction = self.reverse_direction(next_direction) 
                backward.push(reverse_direction)
                player.travel(next_direction)
                path.append(next_direction)
            except:         
                next_direction = backward.pop()
                player.travel(next_direction)
                path.append(next_direction)
    #     visited = {set()}
    #     current_room = starting_room_id
    #     previous_room = None
    #     next_room = None
    #     forward = Stack()
    #     backward = Stack()
    #     forward_counter = 0
    #     reverse_counter = 0
    #     path = []
    #     all_visited = True

    #     # First Call
    #     exit_direction_list = list(self.get_neighbors(current_room).keys())
    #     self.next_direction_1(exit_direction_list, current_room, forward, backward)
    #     visited.add(current_room)

    #     print("path, room, visited")
    #     while len(visited) < len(graph):
    #         print(len(path), current_room, len(visited))
    #         if len(path) == 344:
    #             print("here")
    #         if self.check_neighbors_for_dead_end(exit_direction_list, current_room) == True or next_room in visited: # Backward
    #             if reverse_counter == forward_counter:
    #                 next_room = graph[current_room][1][forward.peek()]
    #                 if next_room in visited:
    #                     backward.pop()
    #                     forward.pop()
    #                 continue
    #             next_direction = backward.pop()
    #             path.append(next_direction)
    #             reverse_counter += 1
    #             next_room = graph[current_room][1][next_direction] 
    #             previous_room = current_room
    #             current_room = next_room
    #             exit_direction_list = list(self.get_neighbors(current_room).keys())
    #             if self.check_neighbors_for_dead_end(exit_direction_list, current_room) == True:
    #                 next_room = graph[current_room][1][backward.peek()]
    #             else:
    #                 next_room = graph[current_room][1][forward.peek()]
    #                 if next_room in visited:
    #                     backward.pop()
    #                     forward.pop()
    #         else: # Forward
    #             next_direction = forward.pop()
    #             opposite_direction = self.reverse_direction(next_direction)
    #             next_room = graph[current_room][1][next_direction]
    #             try:
    #                 graph[next_room][1][opposite_direction]
    #                 path.append(next_direction)
    #                 forward_counter += 1
    #                 self.rooms[current_room][next_direction] = next_room 
    #                 self.rooms[next_room][opposite_direction] = current_room
    #                 previous_room = current_room
    #                 current_room = next_room
    #                 visited.add(current_room)
    #             except:
    #                 self.rooms[current_room][next_direction] = next_room
    #                 backward.pop()                
    #             exit_direction_list = list(self.get_neighbors(current_room).keys())
    #             self.next_direction_1(exit_direction_list, current_room, forward, backward)
    #             if self.check_neighbors_for_dead_end(exit_direction_list, current_room) == False:
    #                 next_room = graph[current_room][1][forward.peek()]
    #                 if next_room in visited:
    #                     backward.pop()
    #                     forward.pop()
    #                     self.rooms[current_room][forward.peek()] = next_room
    #                     try:
    #                         self.rooms[next_room][self.reverse_direction(forward.peek())] = current_room
    #                     except:
    #                         pass
    #     return path

    # def check_neighbors_for_dead_end(self, exit_direction_list, current_room):
    #     dead_end = True
    #     for direction in exit_direction_list:
    #         if self.get_neighbors(current_room)[direction] == '?':
    #             dead_end = False
    #     return dead_end

    # def next_direction_2(self, exit_direction_list, current_room, forward, backward, visited):
    #     for direction in exit_direction_list:
    #         if self.get_neighbors(current_room)[direction] == '?':
    #             if current_room in visited:
    #                 break
    #             else:
    #                 forward.push(direction)
    #                 backward.push(self.reverse_direction(direction))

    # def next_direction_1(self, exit_direction_list, current_room, forward, backward):
    #     for direction in exit_direction_list: #n
    #         if self.get_neighbors(current_room)[direction] == '?': 
    #             forward.push(direction)
    #             backward.push(self.reverse_direction(direction))

    def reverse_direction(self, direction):
        if direction == 'n':
            return 's'
        elif direction == 's':
            return 'n' #this -> n
        elif direction == 'w':
            return 'e'
        else: # direction == 'e'
            return 'w'

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
# traversal_path = []
graph = RoomGraph()
for room in room_graph:
    graph.add_room(room, list(room_graph[room][1].keys()))

print("Class:", graph.rooms)
print("Neighbors:", graph.get_neighbors(0))
# print("DFT:", graph.dft(player.current_room.id, room_graph, player))
traversal_path = graph.dft(player.current_room.id, room_graph, player)

# TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

print("Room:::", player.current_room.id)
print("Exit:::", player.current_room.get_exits())
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
