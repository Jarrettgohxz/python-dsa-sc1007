import sys
import os 

# Add the parent directory of `concepts` to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from concepts.linkedlist.linkedlist import LinkedList

linked_list = LinkedList()

# items = (1, 2, 2, 4, 4, 5, 5)
# items = (1, 2, 3, 4, 5)
items = (1,2,2,2,2,4,4,5,6,6,7,8,8,8,8)

size = 0

for item in items:
 linked_list.insert(item, size)
 size+=1

print("[INFO] Current linked list:", end="\n")
linked_list.display()


# eg. 1,2,2,4,4,5,5 -> 1,2,4,4,5,5
def removeDuplicatesSortedLL(ll:LinkedList):
 items = ll.get_items()
 occured = []
 
 index = 0
 
 for item in items:
  if item not in occured:
   occured.append(item)
   index+=1
  
  else:
   ll.remove_node_at(index)
 
 
removeDuplicatesSortedLL(linked_list)
linked_list.display()