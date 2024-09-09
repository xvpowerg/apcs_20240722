class Node:
    def __init__(self, data=None):
        self.data=data
        self.left=None
        self.right=None     
    def preorder(self):
        print(self.data, end='->')
        if self.left:
            self.left.preorder()
        if self.right:
            self.right.preorder()
    def inorder(self):
        if self.left:
            self.left.inorder()        
        print(self.data, end='->')
        if self.right:
            self.right.inorder()
    def insert(self,data):
        if self.data:
            if data < self.data:
                if self.left:
                    self.left.insert(data)
                else:
                   self.left = Node(data)
            else:
                if self.right:
                    self.right.insert(data)
                else:
                    self.right = Node(data)
        else:
            self.data = data
    
    def search(self,val):
        if val < self.data:
            if not self.left:
                return f"{val}不存在"
            return self.left.search(val)
        elif val > self.data:
            if not self.right:
                return f"{val}不存在"
            return self.right.search(val)
        else:
            return f"找到{val}"
    def minNode(self):
        ptr = self
        while ptr.left:
            ptr = ptr.left
        return ptr
    def delete(self,val):
        if val < self.data:
            if self.left:
                self.left = self.left.delete(val)
            else:
                print(val,"不存在")
        elif val > self.data:
            if self.right:
                self.right = self.right.delete(val)
            else:
                print(val,"不存在")
        else:
            if not self.left:
                tmp = self.right
                self.data = None
                return tmp
            elif  not self.right:
                tmp = self.left
                self.data = None
                return temp
            else:
               tmp = self.right.minNode()
               self.data = tmp.data
               if self.right.data == tmp.data: 
                    self.right = None
               else:
                   self.right.delete(tmp.data)
bast = Node()
datas = [20,15,17,30,32,27,4]
for d in datas:
    bast.insert(d)    

bast.preorder()
print()
bast.inorder()
print()
print(bast.search(30))
print(bast.search(12))
bast.delete(30)
bast.preorder()
