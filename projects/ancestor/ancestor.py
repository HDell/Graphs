
def earliest_ancestor(ancestors, starting_node): # ([(parent, child), (parent, child), (parent, child)], 6)
    graph = Graph()
    # initialize graph, inverting parents and children
    for pair in ancestors:
        if pair[1] not in graph.vertices.keys():
            graph.add_vertex(pair[1])
            graph.add_edge(pair[1], pair[0])
        else:
            graph.add_edge(pair[1], pair[0])
        if pair[0] not in graph.vertices.keys():
            graph.add_vertex(pair[0])
    earliest_ancestor = graph.dft(starting_node)
    # last = graph.dfs(starting_node, earliest_ancestor)[-1]
    if starting_node != earliest_ancestor:
        # return last
        return earliest_ancestor
    else:
        return -1

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