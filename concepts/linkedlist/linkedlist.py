class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

       
    def display(self):
        # get the first node (self.head)
        current = self.head
      
          # while there is still a next node (assigned from the line current = current.next)
        while current:
            print(current.data, end=" -> ")
            current = current.next
            
        print("NONE")
    
    def getsize(self):
        current = self.head
        
        size = 0
        
        while current:
            current = current.next
            size+=1
        
        return size
    
        
    def insert_at_front(self, data):
        new_node = Node(data)
        current_head = self.head
        
        if current_head:
            new_node.next = current_head
        
        self.head = new_node        
        return 1
        

    def insert(self, data, index):
        new_node = Node(data)

        if self.head is None or index == 0:
            
            new_node.next = self.head
            self.head = new_node
            return 1
    
        current = self.head
        count = 0
    
        while current and count < index - 1:
            current = current.next
            count += 1
    
        if not current:
            print("Index out of range")
            return 0
        
        new_node.next = current.next
        current.next = new_node
        return 1
    

        
    def insert_at_back(self, data):
        new_node = Node(data)
        current = self.head
       
        if not current:
           self.head = new_node
           return 1
           
        else:
           while True:
               if not current.next:
                   current.next = new_node
                   break
                
               current = current.next

        return 1


    def findAt(self, index):
        # get first node
        current = self.head
        
        if not current:
            return None

        # iterate through index
        while index > 0:
            current = current.next

            if not current:
                print("Index out of range")
                return None

            index-=1

        return current
    
    def get_items(self):
        current = self.head
        
        items = []
        
        while current:
            items.append(current.data)
            current = current.next
            
        return items
    
    def remove_node_at(self, index):
            
        current = self.head
        
        if index == 0:
            self.head = current.next
            return 1
        
        # iterate until the current node is 1 before the specified node index
        while (index-1) > 0:
            current = current.next
            
            if not current:
                return 0
        
            index-=1
        
        node_to_del = current.next
        current.next = node_to_del.next
        
        del node_to_del
        return 1
       
# Test the implementationW
if __name__ == "__main__":
    linked_list = LinkedList()
    size = 0
    
    print("Enter one number per line (press Enter after each number).")
    print("Enter any non-digit character to finish input:")
    
    while True:
        try:
            item = int(input())
            
            if linked_list.insert(item, size) == 1:
                size += 1
                print("Node successfully inserted")
                
            else:
                print("Insertion failed")
              
            
        # To catch non-integer input - signal to stop program
        except ValueError:
            print("\n[!] Non-integer input detected, stopping program...\n")
            break
        
    print("[INFO] Current linked list:", end="\n")
    linked_list.display()
    print('\n')
    
    # print(f'size before: {linked_list.getsize()}')
    # linked_list.remove_node_at(4)

        
    # print("[AFTER] linked list:", end="\n")
    # linked_list.display()
    # print('\n')
    
    # print(f'size after: {linked_list.getsize()}')
    
    
    

    