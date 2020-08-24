"""

Write a function that, given the dataset and the ID of an individual in the dataset, returns their earliest known ancestor – the one at the farthest distance from the input individual. If there is more than one ancestor tied for "earliest", return the one with the lowest numeric ID. If the input individual has no parents, the function should return -1.

If we wanted the earliest ancestor of 9, we'd traverse up the graph to find 8. From 8, there would be two possible ancestor vertices (4 and 11). We'd keep track of both 4 and 11. If neither 4 nor 11 have any earlier ancestors, we return the ancestor with the lower numeric id (4).

"""

test_ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7),
                  (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]


"""
    PROBLEM: I need to determine all of the earliest ancestors for any starting node if I'm given a list of ancestors. In this case, the correct earliest ancestor is the item in the list which is furthest back in the chain and the smallest possible numeric id.
    
    SOLUTION: I think a dictionary would work well here. I could populate a dictionary with all of the values from the tuples with the key being a child node and the values being a list of possible parent nodes.

    I begin by populating the dictionary with my parent:child pairs. Once I have my dictionary populated, I should have a data structure I can reference easily. We can start with 
"""

# I like to separate the logic of my helper functions out so it doesn't clutter up my main function.


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

    # Recursive algorithm. Need a visited set and a stack.
    stack = []

    # The child dict contains references to each node's parents.
    child_dict = child_table(ancestors)

    # The parent dict contains references to each node's children.
    parent_dict = parent_table(ancestors)

    # We should only be returning a -1 if our original starting node has no parents.
    if starting_node in parent_dict and starting_node not in child_dict:
        print(f"This starting node ({starting_node}) has no parents.")
        return -1

    current_node = starting_node

    # add the starting node to the visited set so we won't backtrack.
    stack.append(current_node)

    while len(stack) > 0:
        print("Here's the item in the stack: ", stack)
        # Remove the item from the stack. We should only have one item at a time because we're only ever
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
