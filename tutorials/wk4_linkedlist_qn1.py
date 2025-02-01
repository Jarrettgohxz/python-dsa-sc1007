import sys
import os 

# Add the parent directory of `concepts` to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from concepts.linkedlist.linkedlist import LinkedList

linked_list = LinkedList()

# items1 = (2, 3, 4, 7, 15, 18)
# items2 = (2, 7, 18, 3, 4, 15)
# items3 = (1, 3, 5)
# items4 = (2, 4, 6)
items = (1,2,3,4,5,6,7,88)

size = 0

for item in items:
 linked_list.insert(item, size)
 size+=1

print("[INFO] Current linked list:", end="\n")
linked_list.display()

def move_even_items_to_back(ll: LinkedList):
 ll_len = ll.getsize()
 
 count = 0
 
 for _ in range(ll_len):
 
  cur = ll.findAt(count)
  
  # check if even
  if ((cur.data%2) == 0):
   
   # if node is shifted to the back, current node index remains the same
   ll.remove_node_at(count)
   ll.insert_at_back(cur.data)
   continue
  
  # increasen the node index only if no node is shifted to the back
  count+=1
 

move_even_items_to_back(linked_list)
linked_list.display()