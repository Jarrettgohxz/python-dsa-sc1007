class BTNode:
    def __init__(self, item, left=None, right=None):
        self.item = item  # Store the item (integer)
        self.left = left  # Reference to the left child node
        self.right = right  # Reference to the right child node


def insertBSTNode(root, value):
    if root is None:
        root = BTNode(value)
        return root

    cur = root

    while True:
        if value < cur.item:
            if cur.left is not None:
                cur = cur.left

            else:
                cur.left = BTNode(value)
                break

        else:
            if cur.right is not None:
                cur = cur.right

            else:
                cur.right = BTNode(value)
                break

    return root


def printTree(node, level=0, prefix="Root: "):
    """Prints the tree structure for better visualization"""
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

        except ValueError:
            print("Please enter a valid integer!")

    print("\nFinal BST structure:")
    printTree(root)
