import random
import time

"""
Helper Classes
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

class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        self.vertices[v1].add(v2)

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        return self.vertices[vertex_id]

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        visited = set()
        queue = Queue()
        queue.enqueue(starting_vertex)
        while queue.size() > 0:
            current = queue.dequeue()
            print(current)
            visited.add(current)
            for neighbor in self.get_neighbors(current):
                if neighbor not in visited:
                    queue.enqueue(neighbor)

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        visited = set()
        stack = Stack()
        stack.push(starting_vertex)
        current = None
        while stack.size() > 0:
            only_ancestors = True
            sorted_neighbors = []
            current = stack.pop()
            if current not in visited:
                print(current)
                visited.add(current)
            for neighbor in self.get_neighbors(current):
                sorted_neighbors.append(neighbor)
                if len(self.get_neighbors(neighbor)) > 0:
                    only_ancestors = False
            sorted(sorted_neighbors)
            for i in range(len(sorted_neighbors)):
                if only_ancestors:
                    neighbor = sorted_neighbors[len(sorted_neighbors)-(i+1)]
                else:
                    neighbor = sorted_neighbors[i]
                if neighbor not in visited:
                    stack.push(neighbor)
        return current

    def dft_recursive(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        print(starting_vertex)
        self.vertices[starting_vertex].add("Visited")
        for neighbor in self.get_neighbors(starting_vertex):
            if (type(neighbor) is int) and ("Visited" not in self.get_neighbors(neighbor)):
                self.dft_recursive(neighbor)


    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        visited = set()
        queue = Queue()
        queue.enqueue([starting_vertex])
        while queue.size() > 0:
            current_path = queue.dequeue()
            last_vertex = current_path[-1]
            if last_vertex not in visited:
                if last_vertex == destination_vertex:
                    return current_path
                else:
                    visited.add(last_vertex)                   
            for neighbor in self.get_neighbors(last_vertex):
                path_copy = list(current_path)
                path_copy.append(neighbor)
                queue.enqueue(path_copy)

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        visited = []
        stack = Stack()
        stack.push(starting_vertex)
        while stack.size() > 0:
            current = stack.pop()
            if current not in visited:
                visited.append(current)
                if current == destination_vertex:
                    return visited
            for neighbor in self.get_neighbors(current):
                if neighbor not in visited:
                    stack.push(neighbor)

    def dfs_recursive(self, starting_vertex, destination_vertex, visited=None, path=[]): # Walked through it in the debugger and I get it, but it's dizzyingly complicated.
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        if visited is None:
            visited = set()
            path.append(starting_vertex)
        visited.add(starting_vertex)
        # current_vertex = path[-1]
        if starting_vertex == destination_vertex:
            return path
        else:
            for neighbor in self.get_neighbors(starting_vertex):
                if neighbor not in visited:
                    path_copy = list(path)
                    path_copy.append(neighbor)
                    if neighbor == destination_vertex:
                       return path_copy
                        # return self.dfs_recursive(neighbor, destination_vertex, visited, path_copy)
                    else:
                        final_path = self.dfs_recursive(neighbor, destination_vertex, visited, path_copy)
                        final_vertex = final_path[-1]
                        if final_vertex == destination_vertex:
                            return final_path
        return path


class User:
    def __init__(self, name):
        self.name = name

class SocialGraph:
    def __init__(self):
        self.last_id = 0
        self.users = {}
        self.friendships = {}

    def add_friendship(self, user_id, friend_id):
        """
        Creates a bi-directional friendship
        """
        if user_id == friend_id:
            print("WARNING: You cannot be friends with yourself")
        elif friend_id in self.friendships[user_id] or user_id in self.friendships[friend_id]:
            print("WARNING: Friendship already exists")
        else:
            self.friendships[user_id].add(friend_id)
            self.friendships[friend_id].add(user_id)

    def add_user(self, name):
        """
        Create a new user with a sequential integer ID
        """
        self.last_id += 1  # automatically increment the ID to assign the new user
        self.users[self.last_id] = User(name)
        self.friendships[self.last_id] = set()

    def populate_graph(self, num_users, avg_friendships):
        """
        Takes a number of users and an average number of friendships
        as arguments

        Creates that number of users and a randomly distributed friendships
        between those users.

        The number of users must be greater than the average number of friendships.
        """
        # Reset graph
        self.last_id = 0
        self.users = {}
        self.friendships = {}
        # !!!! IMPLEMENT ME
        if avg_friendships >= num_users:
            print("The average number of friendships must be less than the number of users.")
            return
        elif num_users <= 1:
            print("The number of users must be above 1.")
            return
        else:
        # Add users
            for i in range(num_users):
                # name = input("Enter a name: ")
                # self.add_user(name)
                self.add_user("same_name")

        # Create friendships
        friendships_max = num_users * avg_friendships
        friendships_count = 0

        #randomize the distribution
        random_order_users = []
        for i in range(1, num_users+1):
            random_order_users.append(i)
        random.shuffle(random_order_users)

        for i in random_order_users:
            num_friends = None
            while (num_friends is None) or (((num_friends * 2) + friendships_count) > friendships_max):
                num_friends = random.randint(0, num_users-1)
            for j in range(num_friends):
                friend_id = 0
                while friend_id == 0 or friend_id == i or friend_id in self.friendships[i]:
                    friend_id = random.randint(1, num_users)
                self.add_friendship(i, friend_id)
            friendships_count += num_friends * 2

    def get_all_social_paths_given(self, user_id):
        queue = Queue()
        visited = {}
        queue.enqueue([user_id])
        while queue.size() > 0:
            path = queue.dequeue()
            last_vertex = path[-1]
            if last_vertex not in visited:
                visited[last_vertex] = path
                for friend in self.friendships[last_vertex]:
                    path_copy = path.copy()
                    path_copy.append(friend)
                    queue.enqueue(path_copy)
        return visited

    def get_all_social_paths(self, user_id):
        """
        Takes a user's user_id as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """
        visited = {}  # Note that this is a dictionary, not a set
        # !!!! IMPLEMENT ME
        visited[user_id] = [user_id]
        graph = Graph()
        for key in self.users.keys():
            graph.add_vertex(key)
            for friend in self.friendships[key]:
                graph.add_edge(key, friend)
        self.get_neighbors_recursively(user_id, user_id, visited, graph)
        return visited


    def get_neighbors_recursively(self, original_vertex, vertex, visited, graph=Graph()):
        for neighbor in graph.get_neighbors(vertex):
            if neighbor not in visited.keys():
                visited[neighbor] = graph.bfs(original_vertex, neighbor)
                self.get_neighbors_recursively(original_vertex, neighbor, visited, graph)

# if __name__ == '__main__':
#     sg = SocialGraph()
#     sg.populate_graph(10, 2)
#     print(sg.friendships)
#     connections = sg.get_all_social_paths(1)
#     print(connections)

if __name__ == '__main__':
    sg = SocialGraph()
    sg.populate_graph(500, 5)
    # print(sg.friendships)
    start_time = time.time()
    connections = sg.get_all_social_paths(1)
    end_time = time.time()
    print("My Function's Runtime:", (end_time - start_time))
    start_time = time.time()
    connections = sg.get_all_social_paths_given(1)
    end_time = time.time()
    print("Given Function's Runtime:", (end_time - start_time))
    # print(connections)

"""
1. To create 100 users with an average of 10 friends each, I would need to call add_friendship() 500 times because the number of friendships that would be created would be
100 * 10, which is 1000. And because each add_friendship creates 2 friendships (one in each direction), the number of calls would be quotient of 1000 / 2.

2. 
15.8% of other users will be in a particular user's extended social network over 50% of the time.
The average degree of seperation between a user and an extended friend is 2.
Logic found in prob.py.
"""