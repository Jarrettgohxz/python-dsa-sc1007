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
    # perform pre-order traversal
    print('', end='\n')

    # node.left.left.left, node.left.left.right, node.left.right.left, ...

    # to prevent repeat printing for nodes with great-grandchild on both left and right subtree
    global greatgrandchildnodes
    greatgrandchildnodes = []

    def recurse(first, cur, n):
        global greatgrandchildnodes

        if cur is None:
            return

        # explored 3 nodes down and current node is NOT None
        if n == 3 and first.item not in greatgrandchildnodes:
            print(first.item)
            greatgrandchildnodes.append(first.item)
            return

        n += 1

        recurse(first, cur.left, n)
        recurse(first, cur.right, n)

    def pre_order_traversal(cur_node):
        if cur_node is None:
            return

        recurse(cur_node, cur_node, 0)

        pre_order_traversal(cur_node.left)
        pre_order_traversal(cur_node.right)

    pre_order_traversal(node)


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
