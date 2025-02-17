class Queue:
    def __init__(self):
        self.top = None
        # ...


def level_order_traversal(self):
    if self.root is None:
        return

    queue = Queue()
    queue.enqueue(self.root)

    while not queue.is_empty():
        node = queue.dequeue()
        print(node.data, end='')

        # process the node...

        if (node.left):
            queue.enqueue(node.left)

        if (node.right):
            queue.enqueue(node.right)


def count_nodes(self, node):
    if node is None:
        return 0

    return 1 + self.count_nodes(node.left) + self.count_nodes(node.right)


def kth_level_descendants(self, node, k):
    if node is None:
        return []

    if k == 0:
        return [node.data]

    k -= 1
    left_descendant = kth_level_descendants(node.left, k)
    right_descendant = kth_level_descendants(node.right, k)

    return left_descendant + right_descendant


def calculate_height(self, node):
    #
    # The height of a tree: The number of edges on the longest path from the root to a leaf
    #

    if node is None:
        # if node doesn't exist, immediately return -1
        # for recursive function call: return -1 instead of 0 since (1 + (-1) = 0 as from the return 1 + ... return statement at the end)

        # since this function counts the number of edges - if the node argument passed to the current recursive call falls on a leaf,
        # the edge should be reduced by 1
        return -1

    # recursively traverse left and right side
    height_left = calculate_height(node.left)
    height_right = calculate_height(node.right)

    # addition of 1 - since this function is called recursively for each layer
    # add the longest path from either left or right side
    return 1 + (height_left if height_left > height_right else height_right)
    # OR return 1 + max(height, left, height_right)
