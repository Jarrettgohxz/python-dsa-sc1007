class BTNode:
    def __init__(self, item, left=None, right=None):
        self.item = item  # Store the item (integer)
        self.left = left  # Reference to the left child node
        self.right = right  # Reference to the right child node


def insertBSTNode(root, value):
    """ Recursive approach to insert a node into a BST. """
    if root is None:
        return BTNode(value)

    if value < root.item:
        root.left = insertBSTNode(root.left, value)
    elif value > root.item:
        root.right = insertBSTNode(root.right, value)
    return root  # Ensure the modified node is returned


def findMin(node):
    """ Find the node with the smallest value in a subtree. """
    while node.left is not None:
        node = node.left
    return node


def removeBSTNode(root, value):
    """
    Returns the updated root node and a result code (0 for success, -1 for failure).
    """
    if root is None:
        return -1

    to_remove = None
    left = 1

    # traverse left
    if value < root.item:
        if root.left.item == value:
            to_remove = root.left

        else:
            removeBSTNode(root.left, value)

    # traverse right:
    else:
        if root.right.item == value:
            to_remove = root.right

        else:
            removeBSTNode(root.right, value)

    # node to remove has no children
    if to_remove.left is None and to_remove.right is None:
        # if ()

    return 0


def printBSTInOrder(node):
    """ Print BST items in sorted order using in-order traversal. """
    if node:
        printBSTInOrder(node.left)
        print(node.item, end=" ")
        printBSTInOrder(node.right)


def printTree(node, level=0, prefix="Root: "):
    """ Pretty prints the tree structure for better visualization """
    if node is not None:
        print(" " * level + prefix + str(node.item))
        if node.left or node.right:
            if node.left:
                printTree(node.left, level + 4, "L--- ")
            if node.right:
                printTree(node.right, level + 4, "R--- ")


if __name__ == "__main__":
    root = None
    print("Binary Search Tree Node Removal Program")
    print("=====================================")

    print("\nFirst, let's build the BST:")
    while True:
        try:
            value = input("\nEnter a value to insert (-1 to quit): ")
            if not value:
                continue  # Ignore empty inputs

            i = int(value)
            if i == -1:
                break

            root = insertBSTNode(root, i)
            print("\nCurrent BST structure:")
            printTree(root)
            print("\nIn-order traversal: ", end="")
            printBSTInOrder(root)
            print()

        except ValueError:
            print("Invalid input! Please enter an integer.")

    print("\nNow let's remove nodes:")
    while True:
        try:
            value = input("\nEnter a value to remove (-1 to quit): ")
            if not value:
                continue  # Ignore empty inputs

            i = int(value)
            if i == -1:
                break

            root, result = removeBSTNode(root, i)
            if result == 0:
                print("\nBST structure after removal:")
                printTree(root)
                print("\nIn-order traversal: ", end="")
                printBSTInOrder(root)
                print()
            else:  # result == -1
                print("Value not found in the tree!")

        except ValueError:
            print("Invalid input! Please enter an integer.")
