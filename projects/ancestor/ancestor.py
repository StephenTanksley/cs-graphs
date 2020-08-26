
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
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):

        # Create the new key with the vertex ID and set the value to an empty set.
        if vertex_id not in self.vertices:
            self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):

        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)

    def add_bidirected_edge(self, v1, v2):
        self.add_edge(v1, v2)
        self.add_edge(v2, v1)

    def get_neighbors(self, vertex_id):

        return self.vertices[vertex_id]

    def bft(self, starting_vertex):

        # path = []
        string = ""

        # STEP 1: Create a queue
        queue = Queue()

        # STEP 2: Need to track visited vertices.
        visited = set()

        # STEP 3: Enqueue the starting vertex.
        queue.enqueue(starting_vertex)

        # while queue is not empty:
        while queue.size() > 0:

            # get current vertex (dequeue from queue)
            current_vertex = queue.dequeue()

            # check if the current vertex has not been visited:
            if current_vertex not in visited:

                # mark the current vertex as visited
                visited.add(current_vertex)

                # print current vertex
                print(current_vertex)

                # path.append(current_vertex)
                string += str(current_vertex)
                string += '\n'

                # Get the neighbors of the current vertex.
                neighbors = self.get_neighbors(current_vertex)

                for i in neighbors:
                    queue.enqueue(i)

        return string

    def dft(self, starting_vertex):

        # This represents the path we've taken to get where we want to go.
        path = []

        # STEP 1: Create a stack.
        stack = Stack()

        # STEP 2: Add a 'visited' set to weed out duplicates.
        visited = set()

        # STEP 3: Add the starting vertex.
        stack.push(starting_vertex)

        # while queue is not empty:
        while stack.size() > 0:

            # set the current vertex to the dequeued element.
            current_vertex = stack.pop()

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

        return path

    def dft_recursive(self, starting_vertex, visited=None, path=None):

        if path is None:
            path = []

        if visited is None:
            visited = set()

        visited.add(starting_vertex)
        neighbors = self.get_neighbors(starting_vertex)

        print(starting_vertex)

        for neighbor in neighbors:
            if neighbor not in visited:
                self.dft_recursive(neighbor, visited)

    def bfs(self, starting_vertex, destination_vertex):

        # STEP 1: Create a queue
        queue = Queue()

        # STEP 2: Need to track visited vertices.
        visited = set()

        # This represents the path we've taken to get where we want to go.
        path = []

        # STEP 3: Enqueue the starting vertex.
        queue.enqueue({'current_vertex': starting_vertex,
                       'path': [starting_vertex]})

        # while queue is not empty:
        while queue.size() > 0:

            # get current vertex (dequeue from queue)
            current_obj = queue.dequeue()

            current_path = current_obj['path']

            # set the current vertex to the dequeued element.
            current_vertex = current_obj['current_vertex']

            # check if the current vertex has not been visited:
            if current_vertex not in visited:
                if current_vertex == destination_vertex:
                    return current_path

                # mark the current vertex as visited
                visited.add(current_vertex)

                # Get the neighbors of the current vertex.
                neighbors = self.get_neighbors(current_vertex)

                for i in neighbors:

                    # queue up NEW paths with each neighbor.
                    new_path = list(current_path)
                    new_path.append(i)

                    queue.enqueue({
                        'current_vertex': i,
                        'path': new_path
                    })

                # add the current vertex to a visited_set
                visited.add(current_vertex)

        print(path)
        return path

    def dfs(self, starting_vertex, destination_vertex, visited=None):

        # This represents the path we've taken to get where we want to go.
        path = []

        # STEP 1: Create a stack.
        stack = Stack()

        # STEP 2: Add a 'visited' set to weed out duplicates.
        visited = set()

        # STEP 3: Add the starting vertex.
        stack.push(starting_vertex)

        # while queue is not empty:
        while stack.size() > 0:

            # set the current vertex to the dequeued element.
            current_vertex = stack.pop()

            # check if the current vertex has not been visited:
            if current_vertex not in visited:

                if current_vertex == destination_vertex:
                    path.append(current_vertex)
                    return path

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

    def dfs_recursive(self, starting_vertex, destination_vertex, path=[], visited=set()):

        # Add the starting vertex to the visited set.
        visited.add(starting_vertex)

        if starting_vertex == destination_vertex:
            return path

        if len(path) == 0:
            path.append(starting_vertex)

        # create neighbors to work through.

        neighbors = self.get_neighbors(starting_vertex)

        for neighbor in neighbors:

            if neighbor not in visited:
                path.append(neighbor)
                final_path = self.dfs_recursive(
                    neighbor, destination_vertex, path, visited)

                if final_path is not None:
                    return final_path


"""

    '''
       10
     /
    1   2   4  11
     \ /   / \ /
      3   5   8
       \ / \   \
        6   7   9
    '''

Write a function that, given the dataset and the ID of an individual in the dataset, returns their earliest known ancestor – the one at the farthest distance from the input individual. If there is more than one ancestor tied for "earliest", return the one with the lowest numeric ID. If the input individual has no parents, the function should return -1.

"""

# test_ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7),
#    (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]


"""
    PROBLEM: I need to determine all of the earliest ancestors for any starting node if I'm given a list of ancestors. In this case, the correct earliest ancestor is the item in the list which is furthest back in the chain and the smallest possible numeric id.
    
    SOLUTION: I think a dictionary would work well here. I could populate two dictionaries: One with nodes which are children, one with nodes which are parents.
    
    We can begin with the original starting_item and then compare that value to the values in the dictionary.
    
        1) If the starting value is in a parent dict and NOT in a child dict, we should return -1 
            because there isn't an earlier ancestor to be found.
            
            1a) At this point, we have passed one of our first conditions and should set a current_node to that starting node. The current_node will change as we progress through our data structure.
            
        2) If the current_node is in the child dict, this means that we aren't where we want to be just yet. We 
            know we need to traverse further up the tree. We can select the minimum value from our 
            child_dict[current_node] since this is going to return a list of up to 2 elements. We throw that minimum value onto the stack and use that as the current_node.
                
        3) If the current_value is ONLY in the parent dict after we've already started our traversal, we know 
            that we've reached the earliest ancestor. At this point, we can return that current_node.
        
"""

# DICT HELPER FUNCTIONS ---------

# test_ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7),
#                   (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]


# def parent_table(ancestors):
#     # Instantiate a table.
#     table = {}

#     for pair in ancestors:
#         parent = pair[0]
#         child = pair[1]

#         if parent not in table:
#             table[parent] = [child]
#         else:
#             table[parent].append(child)
#     return table


# def child_table(ancestors):
#     # Instantiate a table.
#     table = {}

#     for pair in ancestors:
#         parent = pair[0]
#         child = pair[1]

#         if child not in table:
#             table[child] = [parent]
#         else:
#             table[child].append(parent)
#     return table


def earliest_ancestor(ancestors, starting_node):
    pass
    # DICT IMPLEMENTATION ------

    # # The child dict contains references to each node's parents.
    # child_dict = child_table(ancestors)

    # # The parent dict contains references to each node's children.
    # parent_dict = parent_table(ancestors)

    # # We should only be returning a -1 if our original starting node has no parents.
    # if starting_node in parent_dict and starting_node not in child_dict:
    #     return -1

    # # Set the current node to the beginning node in the algorithm.
    # # Iterative algorithm. I'll use a stack to keep track of the current element.
    # stack = [starting_node]

    # # This has the soul of a recursive algorithm without __actually__ being recursive.
    # while len(stack) > 0:

    #     # Remove the item from the stack. We should only have one item at a time because we're only ever added one at a time (the minimum value from the parents)
    #     current_node = stack.pop(0)

    #     # if a node is still in the child dict, that means we haven't reached all the way up to the top.
    #     if current_node in child_dict:
    #         parent_min = min(child_dict[current_node])
    #         stack.append(parent_min)

    #     # If a node is in the parent dict and it ISN'T in the child dict, that means we've hit the key we want and should return it.
    #     if current_node in parent_dict and current_node not in child_dict:
    #         return current_node

    # Just a quick little test runner.


# def run_function(arr):
#     for i in range(len(arr) + 1):
#         print(earliest_ancestor(arr, i))


# run_function(test_ancestors)
