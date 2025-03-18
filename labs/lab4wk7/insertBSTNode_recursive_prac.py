class BTNode:
    def __init__(self, item, left=None, right=None):
        self.item = item
        self.left = left
        self.right = right


def insertBSTNode(root, value):
    if root is None:
        root = BTNode(value)
        return root

    # insert left
    if value < root.item:
        if root.left is None:
            new = BTNode(value)
            root.left = new

        else:
            insertBSTNode(root.left, value)

    # insert right
    else:
        if root.right is None:
            new = BTNode(value)
            root.right = new

        else:
            insertBSTNode(root.right, value)

    return root


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
