import sys
import os 

# Add the parent directory of `concepts` to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from concepts.linkedlist.linkedlist import LinkedList

linked_list = LinkedList()

# items = (30, 20, 40, 70, 50)
items = (1,2,3,88,4,5,6,7)

size = 0

for item in items:
 linked_list.insert(item, size)
 size+=1

print("[INFO] Current linked list:", end="\n")
linked_list.display()


def move_max_to_front_method1(ll: LinkedList):
 largest = 0
 index_with_largest_value = None
 
 ll_len = ll.getsize()
 
 for i in range(ll_len):
  cur = ll.findAt(i)
  
  if cur.data > largest:
   largest = cur.data
   index_with_largest_value = i
  
 ll.remove_node_at(index_with_largest_value) 
 ll.insert_at_front(largest)
 

def move_max_to_front_method2(ll: LinkedList):
  largest = 0
  index_with_largest_value = None
  
  items = ll.get_items()
  
  for i, item in enumerate(items):
    if item > largest:
      largest = item
      index_with_largest_value = i
  
  ll.remove_node_at(index_with_largest_value)
  ll.insert_at_front(largest)


# move_max_to_front_method1(linked_list)
# linked_list.display()

move_max_to_front_method2(linked_list)
linked_list.display()