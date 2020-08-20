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

        # Create the new key with the vertex ID and set the value to an empty set.
        if vertex_id not in self.vertices:
            self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """

        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)

    def add_bidirected_edge(self, v1, v2):
        self.add_edge(v1, v2)
        self.add_edge(v2, v1)

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

        # This represents the path we've taken to get where we want to go.
        path = []

        # Create an empty set to track visited vertices. <====== THIS IS VERY IMPORTANT. DON'T GET STUCK IN A LOOP.
        visited = set()

        # Create an empty queue and enqueue the starting_vertex
        queue = Queue()
        queue.enqueue(starting_vertex)

        # while queue is not empty:
        while queue.size() > 0:

            # get current vertex (dequeue from queue)
            first_element = queue.dequeue()

            # set the current vertex to the dequeued element.
            current_vertex = first_element

            # check if the current vertex has not been visited:
            if current_vertex not in visited:

                # mark the current vertex as visited
                path.append(current_vertex)

                # print the current vertex
                print(current_vertex)

                # Get the neighbors of the current vertex.
                neighbors = self.get_neighbors(current_vertex)

                for i in neighbors:
                    queue.enqueue(i)

                # add the current vertex to a visited_set
                visited.add(current_vertex)

        print(path)
        return path

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """

        # This represents the path we've taken to get where we want to go.
        path = []

        # Create an empty set to track visited vertices. <====== THIS IS VERY IMPORTANT. DON'T GET STUCK IN A LOOP.
        visited = set()

        # Create an empty queue and enqueue the starting_vertex
        stack = Stack()
        stack.push(starting_vertex)

        # while queue is not empty:
        while stack.size() > 0:

            # get current vertex (dequeue from queue)
            first_element = stack.pop()

            # set the current vertex to the dequeued element.
            current_vertex = first_element

            # check if the current vertex has not been visited:
            if current_vertex not in visited:

                # mark the current vertex as visited
                path.append(current_vertex)

                # print the current vertex
                print(current_vertex)

                # Get the neighbors of the current vertex.
                neighbors = self.get_neighbors(current_vertex)

                for i in neighbors:
                    stack.push(i)

                # add the current vertex to a visited_set
                visited.add(current_vertex)

        print(path)
        return path

    def dft_recursive(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        pass  # TODO

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        pass  # TODO

        # Create an empty queue and enqueue the starting_vertex
        # Create an empty set to track visited vertices. <====== THIS IS VERY IMPORTANT. DON'T GET STUCK IN A LOOP.

        # while queue is not empty:
        # get current vertex (dequeue from queue)

        # check if the current vertex has not been visited:
        # check if current vertex is DESTINATION.
        # If it IS, stop and return that vertex.
        # print the current vertex
        # mark the current vertex as visited
        # add the current vertex to a visited_set

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        pass  # TODO

    def dfs_recursive(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        pass  # TODO


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
    graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)
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
    # print(graph.dfs_recursive(1, 6))
