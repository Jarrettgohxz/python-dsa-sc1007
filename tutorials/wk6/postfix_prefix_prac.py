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


operator_precedence = (
    '%',
    '*',
    '+',
    '>>',
    '='
)


def postfix_to_prefix(postfix: str):

    S = Stack()

    postfix = postfix.split(' ')

    for i in postfix:
        if i in operator_precedence:
            op1 = S.pop()
            op2 = S.pop()
            exp = f'{i}{op2}{op1}'

            S.push(exp)

        else:
            S.push(i)

    prefix = S.pop()
    print(prefix)


postfix_to_prefix("x a b c * d % + e >> =")
