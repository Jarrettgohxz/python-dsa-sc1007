# x = a + b*c%d >> e

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def findNode(self, index):
        if index < 0 or index >= self.size:
            return None
        if self.head is None:
            return None

        cur = self.head
        while index > 0:
            cur = cur.next
            index -= 1
        return cur

    def insertNode(self, data, index):
        if index < 0 or index > self.size:
            return None

        new_node = Node(data)

        if index == 0:
            new_node.next = self.head
            self.head = new_node
            self.size += 1
            return True

        prev_node = self.findNode(index - 1)
        if prev_node is None:
            return None
        new_node.next = prev_node.next
        prev_node.next = new_node
        self.size += 1
        return True

    def removeNode(self, index):
        if self.head is None:
            return None
        if index < 0 or index >= self.size:
            return None

        if index == 0:
            self.head = self.head.next
            self.size -= 1
            return True

        pre = self.findNode(index - 1)
        if pre is None or pre.next is None:
            return None
        pre.next = pre.next.next
        self.size -= 1
        return True

    def print_list(self):
        cur = self.head
        if cur is None:
            print("Empty")
            return
        while cur is not None:
            print(cur.data, end=" ")
            cur = cur.next
        print("")

    def remove_all_items(self):
        self.head = None
        self.size = 0


class Stack:
    def __init__(self):
        self.ll = LinkedList()

    def push(self, data):
        return self.ll.insertNode(data, 0)

    def pop(self):
        if self.isEmpty():
            return None
        data = self.ll.head.data
        if self.ll.removeNode(0):
            return data
        return None

    def peek(self):
        if self.isEmpty():
            return None
        return self.ll.head.data

    def isEmpty(self):
        return self.ll.size == 0


operator_precedence = {
    '%': 4,
    '*': 4,
    '+': 3,
    '>>': 2,
    '=': 1
}


def infix_to_postfix(infix: str):

    postfix = []
    S = Stack()

    infix = infix.split(' ')

    for i in infix:
        # current value is NOT an operator
        if i not in operator_precedence.keys():
            postfix.append(i)

        # current value is an operator
        else:

            while not S.isEmpty() and operator_precedence[S.peek()] >= operator_precedence[i]:
                postfix.append(S.pop())

            S.push(i)

    while not S.isEmpty():
        postfix.append(S.pop())

    print(" ".join(postfix))


infix_to_postfix("x = a + b * c % d >> e")
