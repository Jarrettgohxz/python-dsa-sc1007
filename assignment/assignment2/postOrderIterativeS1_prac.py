class BSTNode:
   def __init__(self, data):
       self.data = data
       self.left = None
       self.right = None

class StackNode:
   def __init__(self, data):
       self.data = data
       self.next = None

class Stack:
   def __init__(self):
       self.top = None

def insert(root, data):
   if root is None:
       return BSTNode(data)
   
   if data < root.data:
       root.left = insert(root.left, data)
   else:
       root.right = insert(root.right, data)
       
   return root

def push(stack, node):
   temp = StackNode(node)
   if stack.top is None:
       stack.top = temp
       temp.next = None
   else:
       temp.next = stack.top
       stack.top = temp

def pop(stack):
   if stack.top is not None:
       temp = stack.top
       stack.top = temp.next
       return temp.data
   return None

def is_empty(stack):
   return stack.top is None

def peek(stack):
    if stack.top is not None:
        return stack.top.data
    return None


# MY OWN SOLUTION
def postOrderIterativeS1(root):
    if root is None:
        return
    
    S = Stack()
    lastVisitedNode = None
    
    while not is_empty(S) or root is not None:
        # traverse all left nodes
        while root is not None:
            push(S, root)
            root = root.left

        else:
            top = peek(S)
            
            if top.right is not None:
                # right subtree has been visited
                if top.right == lastVisitedNode:
                    top = pop(S)
                    print(top.data, end=" ")
                    lastVisitedNode = top
                    
                # right subtree has NOT been visited
                else:   
                    root = top.right
                    lastVisitedNode = root
                    
            else:
                top = pop(S)
                print(top.data, end=" ") 
            
            # # if top is not None:            
            # # 
            # # if top.right == lastVisitedNode:
            # if top == lastVisitedNode:
            #     top = pop(S)
            #     print(top.data, end=" ")
            #     continue
            
            # # first time traversing right subtree
            # else:      
            #     # top = pop(S)          
            #     root = top.right
            #     # print(root.data, end=" ")
            #     lastVisitedNode = root
            
          
        
    

if __name__ == "__main__":
   root = None
   choice = 1

   print("1: Insert an integer into the binary search tree")
   print("2: Print the post-order traversal of the binary search tree")
   print("0: Quit")

   while choice != 0:
       choice = int(input("\nPlease input your choice(1/2/0): "))
       
       if choice == 1:
           value = int(input("Input an integer to insert: "))
           root = insert(root, value)
       elif choice == 2:
           print("Post-order traversal: ", end="")
           postOrderIterativeS1(root)
           print()
       elif choice == 0:
           break
       else:
           print("Choice unknown")