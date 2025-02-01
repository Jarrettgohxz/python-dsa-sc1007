class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        

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
       
       
       
    def display(self):
        # get the first node (self.head)
        current = self.head
      
          # while there is still a next node (assigned from the line current = current.next)
        while current:
            print(current.data,end=" -> ")
            current = current.next
            
        print("NONE")
    

       
       
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