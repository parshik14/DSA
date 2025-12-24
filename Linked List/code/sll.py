class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

# insertion operation in linklist
# insert at begin , end and specific pos
def insertAtBegin(head,x):
    newNode = Node(x)
    if head is not None:
        newNode.next = head
        head = newNode
    head = newNode

    return newNode

def insertAtEnd(head,x):
    newNode = Node(x)

    temp = head
    while temp.next is not None:
        temp = temp.next
    temp.next = newNode
    return head

# delete in singly linklist
def deleteatfirst(head):
    temp = head
    head = temp.next
    temp = None

    return head
def deleteAtlast(head):
    temp = head
    while temp.next.next is not None:
        temp = temp.next
    temp.next = None

    return head
def deleteatpos(head,pos):
    temp = head
    for i in range(1,pos-1):
        temp = temp.next
    
    temp.next = temp.next.next

    return head
# linked list printing function
def printLL(head):
    temp = head

    while temp is not None:
        print(temp.data)
        temp = temp.next

if __name__ == "__main__":
    head = Node(10)
    head.next = Node(20)
    head.next.next = Node(30)
    head.next.next.next = Node(40)
    head.next.next.next.next = Node(50)

    printLL(head)
    head = deleteatpos(head,3)
    printLL(head)
