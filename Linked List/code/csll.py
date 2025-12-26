class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

# insert
def insertAtBegin(last, x):
    newNode = Node(x)
    # If list is empty, new node points to itself and becomes last
    if last is None:
        newNode.next = newNode
        return newNode

    newNode.next = last.next
    last.next = newNode
    return last

def insertAtEnd()

def printLL(last):
    if last is None:
        return
    temp = last.next
    while True:
        print(temp.data)
        temp = temp.next
        if temp == last.next:
            break
    
if __name__ == "__main__":
    head = Node(10)
    head.next = Node(20)
    head.next.next = Node(30)
    head.next.next.next = Node(40)

    last = head.next.next.next
    last.next = head

    last = insertAtBegin(last, 5)
    printLL(last)
