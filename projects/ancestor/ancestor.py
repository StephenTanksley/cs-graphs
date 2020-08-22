"""

 10
 /
1   2   4  11
 \ /   / \ /
  3   5   8
   \ / \   |
    6   7   9


Write a function that, given the dataset and the ID of an individual in the dataset, returns their earliest known ancestor – the one at the farthest distance from the input individual. If there is more than one ancestor tied for "earliest", return the one with the lowest numeric ID. If the input individual has no parents, the function should return -1.

If we wanted the earliest ancestor of 9, we'd traverse up the graph to find 8. From 8, there would be two possible ancestor vertices (4 and 11). We'd keep track of both 4 and 11. If neither 4 nor 11 have any earlier ancestors, we return the ancestor with the lower numeric id (4).

"""

test_ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7),
                  (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]


"""
    PROBLEM: I need to determine all of the earliest ancestors for any starting node if I'm given a list of ancestors. In this case, the correct earliest ancestor is the item in the list which is furthest back in the chain and the smallest possible numeric id.
    
    SOLUTION: I think a dictionary would work well here. I could populate a dictionary with all of the values from the tuples with the key being a child node and the values being a list of possible parent nodes.

    I begin by populating the dictionary with my parent:child pairs. Once I have my dictionary populated, I should have a data structure I can reference easily.
    
    THE PROGRAM:
    
    set current_node = starting_node
    
    if current_node has no parents:
        return -1
    
    while current_node has parents:
        1) check the value of each parent node.
        2) Find the node with the lower id value.
        3) set the current node to that node.
        
    return current_node

"""

# I like to separate the logic of my helper functions out so it doesn't clutter up my main function.


def build_table(ancestors):

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

    # Get a reference to our data structure at the beginning.
    table = build_table(ancestors)

    print(table)

    """
    starting_node = 9
    current_node = starting_node
    
    If I'm starting at node 9, that means the only possible parent at that case will be node 8.
    
    table[9] = [8]
    
    So the smallest possible parent node for 9 will be 8.
    
    smallest_parent = min(table[current_node])
    
    
    # We want to reassign the current node so now we're looking at the next level up in the list.
    current_node = smallest_parent
    
    
    
    """

    # Breaking condition - if our starting node has no parents. This could only happen in the test case if our input node was 10.

    if starting_node not in table:
        return -1

    if len(table[starting_node]) == 0:
        return -1

    # # set our current node. This value will change as we move along the table.
    # current_node = starting_node

    # while len(table[current_node]) != 0:

    #     # We always want to be taking the smaller parent as the
    #     smaller_parent = min(table[current_node])
    #     current_node = smaller_parent

    # return current_node


earliest_ancestor(test_ancestors, 10)
