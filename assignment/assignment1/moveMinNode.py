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
        new_node.next = prev_node.next
        prev_node.next = new_node
        self.size += 1
        return True

    def printList(self):
        cur = self.head
        if cur is None:
            print("Empty")
            return
        while cur is not None:
            print(cur.data, end=" -> ")
            cur = cur.next
        print("None")


def moveMinNode(head):
    lowest_v = head.data
    start = False  # holds the boolean value to indicate that the initial iteration to find the lowest value is already done

    while True:
        # reset
        cur = head

        while cur.next:

            if start and cur.next.data == lowest_v:
                node_to_shift = cur.next
                new_next = cur.next.next

                node_to_shift.next = head
                head = node_to_shift
                cur.next = new_next

        # only increase node index if no node was removed -> cur = cur.next line ran at the end of loop
        # the operation that removes the next node assigns a new next node - to ensure that consecutive low values will be accounted for; example 2 3 1 1 5 (ensure the consecutive 1s will be accounted)
        # eg. when the cur.data is 3 -> the cur.next.data (value 1) will be removed, the next will also be a value 1 -> if cur=cur.next is applied the new node will be 1 and itself won't be checked (and will not be shifted to the front)
                continue

            elif cur.next.data < lowest_v:
                lowest_v = cur.next.data

            cur = cur.next

            if not cur:
                break

        if start:
            break
        # change start value to True
        else:
            start = True

    return head


if __name__ == "__main__":
    linked_list = LinkedList()

    print("Enter a list of numbers, terminated by any non-digit character: ", end="")
    input_string = input()
    numbers = input_string.split()

    counter = 0
    for num in numbers:
        try:
            linked_list.insertNode(int(num), counter)
            counter += 1
        except ValueError:
            break


print("\nBefore:", end=" ")
linked_list.printList()

linked_list.head = moveMinNode(linked_list.head)
print("After:", end=" ")
linked_list.printList()

print("\nBefore:", end=" ")
linked_list.printList()

linked_list.head = moveMinNode(linked_list.head)
print("After:", end=" ")
linked_list.printList()
