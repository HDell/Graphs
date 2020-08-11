"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy

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
        while stack.size() > 0:
            current = stack.pop()
            if current not in visited:
                print(current)
                visited.add(current)
            for neighbor in self.get_neighbors(current):
                if neighbor not in visited:
                    stack.push(neighbor)

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

    def dfs_recursive(self, starting_vertex, destination_vertex, visited=None, path=[]): # Solved by messing around w/ it. Don't FULLY understand why it works, but it works.
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
        

if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    #graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    # graph.dft(1)
    # graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    # print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    # print(graph.dfs(1, 6))
    print(graph.dfs_recursive(1, 6))
