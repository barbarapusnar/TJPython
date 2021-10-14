from treelib import Node, Tree
def minmax(tree, current_id, is_max):
    '''
    tree: tree object to minmax over
    current_id: current_id where we are in the tree
    is_max: are we the maximizing player?
    '''
    if tree.depth(current_id) == tree.depth():             # If this holds, we are at the end of the tree
        return int(tree[current_id].tag)                   # return the value at the end of tree so it propagates up the tree
    children_of_current_id = tree.children(current_id)     # Determine the children of the current node
    scores = [minmax(tree, child.identifier, not is_max) for child in children_of_current_id]   # Recursively run this function on each of the children
    if is_max:                                             # Return the appropriate score for the max or min player  
        return max(scores)
    else:
        return min(scores)
tree = Tree()
tree.create_node("root", "root")
tree.create_node("", "l1", parent='root')
tree.create_node("", "r1", parent='root')
tree.create_node("3", "l1-1", parent='l1')
tree.create_node("5", "l1-2", parent='l1')
tree.create_node("2", "r1-1", parent='r1')
tree.create_node("9", "r1-2", parent='r1')

tree.show()


print(minmax(tree, 'root', True))