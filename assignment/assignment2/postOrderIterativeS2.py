class BSTNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class StackNode:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.top = None


def insert(root, data):
    if root is None:
        return BSTNode(data)

    if data < root.data:
        root.left = insert(root.left, data)
    else:
        root.right = insert(root.right, data)

    return root


def push(stack, node):
    temp = StackNode(node)
    if stack.top is None:
        stack.top = temp
        temp.next = None
    else:
        temp.next = stack.top
        stack.top = temp


def pop(stack):
    if stack.top is not None:
        temp = stack.top
        stack.top = temp.next
        return temp.data
    return None


def is_empty(stack):
    return stack.top is None


def postOrderIterativeS2(root):

    if root is None:
        return

    S1 = Stack()  # store current nodes
    S2 = Stack()  # store nodes to print in reverse order

    while not is_empty(S1) or root is not None:

        # iterate through right nodes - retrieved in reverse order -> notice is not left nodes
        # run loop until no more right nodes
        while root is not None:
            push(S1, root)  # push to S1 to pop and process later on
            push(S2, root)  # directly push to stack S2
            root = root.right

        # start processing the nodes in S1
        else:

            # not peek - but pop instead without pushing into stack S2 -> alr pushed in the while loop above
            # simply pop to process the left nodes
            top = pop(S1)

            # make the node to the left of the current top node in S1 to be the new root node
            if top is not None:
                root = top.left

    # simply print the post-order traversal
    while not is_empty(S2):
        node = pop(S2)
        print(node.data, end=" ")


if __name__ == "__main__":
    root = None
    choice = 1

    print("1: Insert an integer into the binary search tree")
    print("2: Print the post-order traversal of the binary search tree")
    print("0: Quit")

    while choice != 0:
        choice = int(input("\nPlease input your choice(1/2/0): "))

        if choice == 1:
            value = int(input("Input an integer to insert: "))
            root = insert(root, value)
        elif choice == 2:
            print("Post-order traversal: ", end="")
            postOrderIterativeS2(root)
            print()
        elif choice == 0:
            break
        else:
            print("Choice unknown")
