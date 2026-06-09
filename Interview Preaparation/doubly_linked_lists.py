# Interview preparation practice module.
# Contains algorithms and data structure exercises for coding interviews.

class Node:
  
    def __init__(self, data):
        # To store the value or data.
        self.data = data

        # Reference to the previous node
        self.prev = None

        # Reference to the next node
        self.next = None

# function to traverse and print the singly linked list
def traverseList(head):
    current = head 
    while current is not None : 
        print(current.data,end = "")
        if current.next is not None : print("<->",end = '')
        current = current.next 
    print("")
def insertAtbeginning(head,newdata) : 
    new_node = Node(newdata)
    new_node.next = head 
    head.prev = new_node
    return new_node

def insertAtend(head,newdata) :
    current = head 
    while current.next is not None :
        current = current.next 
    new_node = Node(newdata)
    current.next = new_node
    new_node.prev = current
    return head 
        
def insert(head,newdata,pos) : 
    current = head 
    if pos == 1 : 
        return insertAtbeginning(head,newdata)
    for _ in range(1,pos-1):
        current = current.next 
    new_node = Node(newdata)
    new_node.prev = current 
    new_node.next = current.next
    current.next = new_node 
    return head 
def delAtbeginning(head) : 
    head = head.next 
    head.prev = None 
    return head
def delAtend(head) : 
    current = head 
    while current.next is not None :
        current = current.next 
    current = current.prev 
    current.next = None 
    return head
        
def delete (head,pos) : 
    current = head 
    if pos == 1 : 
        return delAtbeginning(head)
    for _ in range(1,pos):
        current = current.next 
    current.prev.next = current.next 
    current.next.prev = current.prev
    
    return head 



def reverse(head):
    current = head 
    prev = None 
    while(current is not None) : 
        prev = current.prev
        current.prev = current.next 
        current.next = prev  
        
        current = current.prev 
    return prev.prev
             
    
    
if __name__ == "__main__":
    # Create the first node (head of the list)
    head = Node(10)

    # Create and link the second node
    head.next = Node(20)
    head.next.prev = head

    # Create and link the third node
    head.next.next = Node(30)
    head.next.next.prev = head.next

    # Create and link the fourth node
    head.next.next.next = Node(40)
    head.next.next.next.prev = head.next.next
    traverseList(head)
    head = insertAtbeginning(head,0.3) 
    traverseList(head)
    head = insertAtend(head,-9)
    traverseList(head)
    head = insert(head,-0.85,2) 
    traverseList(head)
    head = delAtbeginning(head)
    traverseList(head)
    head = delAtend(head)
    traverseList(head)
    head = delete (head,4)
    traverseList(head)
    head = reverse(head)
    traverseList(head)

    
