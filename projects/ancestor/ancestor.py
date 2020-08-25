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
#                   (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]


"""
    PROBLEM: I need to determine all of the earliest ancestors for any starting node if I'm given a list of ancestors. In this case, the correct earliest ancestor is the item in the list which is furthest back in the chain and the smallest possible numeric id.
    
    SOLUTION: I think a dictionary would work well here. I could populate a dictionary with all of the values from the tuples with the key being a child node and the values being a list of possible parent nodes.

    I begin by populating the dictionary with my parent:child pairs. Once I have my dictionary populated, I should have a data structure I can reference easily. 
    
    We can start with the original starting item and then compare that value to the values in the dictionary.
        1) If the starting value is already in a parent dict and not in a child dict, we should return -1 
            because there isn't an earlier ancestor to be found.
            
        2) If the starting value is in the child dict, we can choose to only pick the minimum value from our 
            child_dict, so we throw that value onto the stack and use that as the current_node.
                
        3) If the starting value is ONLY in the parent dict after we've already started our traversal, we know 
            that 
        
"""

# I like to separate the logic of my helper functions out so it doesn't clutter up my main function.


test_ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7),
                  (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]


def parent_table(ancestors):

    # Instantiate a table.
    table = {}

    for pair in ancestors:
        parent = pair[0]
        child = pair[1]

        if parent not in table:
            table[parent] = [child]
        else:
            table[parent].append(child)
    return table


def child_table(ancestors):
    # Instantiate a table.
    table = {}

    for pair in ancestors:
        parent = pair[0]
        child = pair[1]

        if child not in table:
            table[child] = [parent]
        else:
            table[child].append(parent)
    return table


def earliest_ancestor(ancestors, starting_node):

    # The child dict contains references to each node's parents.
    child_dict = child_table(ancestors)

    # The parent dict contains references to each node's children.
    parent_dict = parent_table(ancestors)

    # We should only be returning a -1 if our original starting node has no parents.
    if starting_node in parent_dict and starting_node not in child_dict:
        return -1

    # Set the current node to the beginning node in the algorithm.
    # Iterative algorithm. I'll use a stack to keep track of the current element.
    stack = [starting_node]

    # This kinda has the soul of a recursive algorithm without actually being recursive.
    while len(stack) > 0:

        # Remove the item from the stack. We should only have one item at a time because we're only ever added one at a time (the minimum value from the parents)
        node = stack.pop(0)

        # if a node is still in the child dict, that means we haven't reached all the way up to the top.
        if node in child_dict:
            parent_min = min(child_dict[node])
            stack.append(parent_min)

        # If a node is in the parent dict and it ISN'T in the child dict, that means we've hit the key we want and should return it.
        if node in parent_dict and node not in child_dict:
            return node


# Just a quick little test runner.
def run_function(arr):
    for i in range(len(arr) + 1):
        print(earliest_ancestor(arr, i))


run_function(test_ancestors)
