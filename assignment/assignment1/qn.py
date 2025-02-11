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
            raise ValueError("Invalid position")
        if self.head is None:
            raise ValueError("List is empty")

        cur = self.head
        while index > 0:
            cur = cur.next
            index -= 1
        return cur

    def insertNode(self, data, index):
        if index < 0 or index > self.size:
            raise ValueError("Invalid position")

        new_node = Node(data)

        if index == 0:
            new_node.next = self.head
            self.head = new_node
            self.size += 1
            return True

        prev_node = self.findNode(index - 1)
        if prev_node is not None:
            new_node.next = prev_node.next
            prev_node.next = new_node
            self.size += 1
            return True
        return False

    def removeNode(self, index):
        if index < 0 or index >= self.size:
            raise ValueError("Invalid position")

        if self.head is None:
            return False

        if index == 0:
            cur = self.head
            self.head = cur.next
            self.size -= 1
            return True

        pre = self.findNode(index - 1)
        if pre is not None and pre.next is not None:
            cur = pre.next
            pre.next = cur.next
            self.size -= 1
            return True
        return False

    def printList(self):
        cur = self.head
        if cur is None:
            print("Empty")
            return
        while cur is not None:
            print(cur.data, end=" -> ")
            cur = cur.next
        print("None")


def moveOdditemstoback(head):
    cur = head
    tail = None

    shifted = []

    # index 0
    if (cur.data % 2 != 0):
        print()

    # emulating a do-while loop
    while True:
        #
        # handle case if index 0 is the one that requires shifting - odd
        #

        print(f'data: {cur.data}')

        # if (not cur.next):
        #     tail = cur
        #     break

        if (cur.next.data % 2 != 0):

            # # no saved tail value
            # if (not tail):

            #     icur = head

            #     while True:
            #         icur = icur.next

            #         if (not icur.next):
            #             tail = icur
            #             break

            shifted.append(cur.next)
            cur.next = cur.next.next

            if (not cur.next):
                tail = cur
                break
            elif (not cur.next.next):
                tail = cur.next
                break

        else:
            if not cur.next.next:
                tail = cur.next
                break

        cur = cur.next

    for s in shifted:
        s.next = None
        tail.next = s
        tail = s

    return head

    # while current:
    #     current = current.next

    #     data = current.data

    #     # if even
    #     if (data % 2 == 0):


if __name__ == "__main__":
    linked_list = LinkedList()

    print("Enter a list of numbers, terminated by any non-digit character: ", end="")
    input_string = input()
    numbers = input_string.split()

    counter = 0
    print(numbers)
    for num in numbers:
        try:
            linked_list.insertNode(int(num), counter)
            counter += 1
        except ValueError:
            break

    print("\nBefore:", end=" ")
    linked_list.printList()
    linked_list.head = moveOdditemstoback(linked_list.head)
    print("After:", end=" ")
    linked_list.printList()
