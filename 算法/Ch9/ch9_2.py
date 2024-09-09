class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
    def preorder(self):
        print(self.data,end="->")
        if self.left:
            self.left.preorder()
        if self.right:
            self.right.preorder()
        
nodeA = Node(14)
nodeB = Node(3)
nodeC = Node(16)
nodeD = Node(23)
nodeE = Node(7)
nodeF = Node(20)
root = nodeA
nodeA.left = nodeB
nodeB.left = nodeC
nodeB.right = nodeD
nodeA.right = nodeE
nodeE.right = nodeF
root = nodeA
root.preorder()

