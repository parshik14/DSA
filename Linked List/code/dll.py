class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None

def printLL(Head):
    temp = head

    while temp is not None:
        print(temp.data)
        temp = temp.next
    return head

# insertion
# at begin
def insertatbegin(head,x):
    newNode = Node(x)
    
    newNode.next = head
    head.prev = newNode
    head = newNode
    return head
# at end
def insertatend(head,x):
    newnode = Node(x)
    temp = head

    while temp.next is not None:
        temp = temp.next
    
    temp.next = newnode
    newnode.prev = temp

    return head

# at pos
def insertatpos(head,pos,x):
    newNode = Node(x)
    temp = head
    for i in range(1,pos-1):
        temp = temp.next
    
    newNode.next = temp.next
    newNode.prev = temp
    temp.next.prev = newNode.next
    temp.next = newNode

    return head

# delete
def deleteAtStart(head):
    
    head = head.next
    head.prev = None

    return head
def deleteAtEnd(head):
    temp = head

    while temp.next is not None:
        temp = temp.next
    temp = temp.prev
    temp.next = None

    return head

def deleteAtPos(head,pos):
    temp = head
    for i in range(1,pos-1):
        temp = temp.next
    temp.prev.next = temp.next
    temp.next.prev = temp.prev

    return head
    
if __name__ == "__main__":
    head = Node(10)

    head.next = Node(20)
    head.next.prev = head

    head.next.next = Node(30)
    head.next.next.prev = head.next

    head.next.next.next = Node(40)
    head.next.next.next.prev = head.next.next

    head=deleteAtPos(head,1)
    printLL(head)


