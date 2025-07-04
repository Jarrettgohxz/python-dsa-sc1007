class BTNode:
    def __init__(self, item, left=None, right=None):
        self.item = item
        self.left = left
        self.right = right

def insertBSTNode(node, value):

    # Only True if the initial function call (not recursive) passes in a root node value that is None
    if node is None:
        return BTNode(value)

    # smaller than current value -> place in left subtree
    if value < node.item:
        if node.left is None:
            new_node = BTNode(value)
            node.left = new_node
        
        else:
            insertBSTNode(node.left ,value)
    
    # larger than current value -> place in right subtree
    else:
        if node.right is None:
            new_node = BTNode(value)
            node.right = new_node
        
        else:
            insertBSTNode(node.right, value)

    # returns the root node value at the end of all the recursive function calls - node has been inserted
    return node


def printTree(node, level=0, prefix="Root: "):
    if node is not None:
        print(" " * level + prefix + str(node.item))
        if node.left or node.right:
            if node.left:
                printTree(node.left, level + 4, "L--- ")
            if node.right:
                printTree(node.right, level + 4, "R--- ")

if __name__ == "__main__":
    root = None
    print("Binary Search Tree Insertion Program")
    print("===================================")
    
    while True:
        value = input("\nEnter a value to insert (-1 to quit): ")
        if not value:
            continue  # Ignore empty inputs
        
        try:
            i = int(value)
            if i == -1:
                break
            
            root = insertBSTNode(root, i)
            print("\nCurrent BST structure:")
            printTree(root)
        
        except ValueError:
            print("Invalid input! Please enter an integer.")

    print("\nFinal BST structure:")
    printTree(root)
