class BTNode:
    def __init__(self, item, left=None, right=None):
        self.item = item
        self.left = left
        self.right = right


def print_tree_in_order(node):
    if node is None:
        return
    print_tree_in_order(node.left)
    print(node.item, end=", ")
    print_tree_in_order(node.right)


def printTree(node, level=0, prefix="Root: "):
    if node is not None:
        print(" " * level + prefix + str(node.item))
        if node.left or node.right:
            if node.left:
                printTree(node.left, level + 4, "L--- ")
            if node.right:
                printTree(node.right, level + 4, "R--- ")


def hasGreatGrandchild(node):
    if node is None:
        return -1

    len = 1 + max(hasGreatGrandchild(node.left),
                  hasGreatGrandchild(node.right))

    if len >= 3:
        print(node.item, end=' ')

    return len


if __name__ == "__main__":
    # Create a tree with nodes having great-grandchildren
    root = BTNode(10)

    # # Left subtree
    # root.left = BTNode(2)
    # root.left.left = BTNode(4)
    # root.left.left.left = BTNode(8)
    # root.left.left.left.left = BTNode(16)

    # # Right subtree
    # root.right = BTNode(3)
    # root.right.right = BTNode(7)
    # root.right.right.right = BTNode(15)
    # root.right.right.right.right = BTNode(31)

    # Left subtree
    root.left = BTNode(20)
    root.left.left = BTNode(40)
    root.left.left.left = BTNode(60)
    root.left.left.left.left = BTNode(90)

    # Right subtree
    root.right = BTNode(30)
    root.right.right = BTNode(50)
    root.right.right.right = BTNode(80)

    print("Visual representation of the tree:")
    printTree(root)

    print("\nTree (In-Order):")
    print_tree_in_order(root)

    print("\nNodes with great-grandchildren:", end=" ")
    hasGreatGrandchild(root)
    print()
