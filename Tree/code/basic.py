class Node:
    def __init__(self,x):
        self.data = x
        self.left = None
        self.right = None

def inorder(node,res):
    if node is None:
        return
    
    inorder(node.left,res)
    res.append(node.data)
    inorder(node.right,res)

def preorder(node,res):
    if node is Node:
        return
    
    res.append(node.data)
    preorder(node.left,res)
    preorder(node.right,res)

def postorder(node,res):
    if node is None:
        return
    postorder(node.left,res)
    postorder(node.right,res)
    res.append(node.data)

if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.right = Node(6)

    res = []

    inorder(root,res)

    print(res)
