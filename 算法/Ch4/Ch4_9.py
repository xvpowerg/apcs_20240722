class Node():        
    def __init__(self,data = None):
        self.data = data
        self.next = None
class LinekdList():
        def __init__(self):
            self.head = Node
        def printList(self):
            ptr = self.head
            while ptr:
                print(ptr.data)
                ptr = ptr.next
myList = LinekdList()
n1 = Node(5)
myList.head = n1
n2 = Node(15)
n3 = Node(25)
myList.head.next = n2
n2.next = n3
myList.printList()
