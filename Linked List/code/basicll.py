class Node : 
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None

def printll(head,pos):
    temp = head
    for i in range(1,pos):
        temp =  temp.next
    print(temp.data)

if __name__ == "__main__":
    head = Node(10)

    head.next = Node(20)
    head.next.prev = head.next

    head.next.next = Node(30)
    head.next.next.prev = head.next.next

    head.next.next.next = Node(40)
    head.next.next.next.prev = head.next.next.next

    head = printll(head,4)
    print(head)

