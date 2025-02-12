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

    # handle negative values at the front
    while True:
        if (cur.data % 2 != 0):
            shifted.append(cur)
            head = cur.next
            cur = head

        else:
            break

    # portion that deals with the rest of list after clearing the negative values at the front
    # cur (head value) will currently be a positive value - so can start checking cur.next
    while True:

        if (cur.next.data % 2 != 0):

            shifted.append(cur.next)
            cur.next = cur.next.next

            if (not cur.next):
                tail = cur
                break

            continue

        else:
            # prevents the first statement in the main while loop from getting error: cur.next.data to be undefined
            # since cur = cur.next is ran on the last else scope
            if not cur.next.next:
                tail = cur.next
                break

            # prevent cur (assigned from cur.next in the last else scope) to be undefined
            elif not cur.next:
                tail = cur
                break

            # simply increment
            else:
                cur = cur.next

    # append the negative values (removed from the main list) to the back
    for s in shifted:
        s.next = None
        tail.next = s
        tail = s

    return head


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
