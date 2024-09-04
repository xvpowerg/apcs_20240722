myList = [5,8,11,2,9]
myList.sort()
print(myList)

class Test1:
    def __init__(self,value):
        self.value = value
    def __str__(self):    
        return str(self.value)
    def __lt__(self,other):
        return self.value < other.value
t1 = Test1(10)
t2 = Test1(8)
t3 = Test1(2)
t4 = Test1(7)
myList2 = [t1,t2,t3,t4]
for v in myList2:
    print(v,end = " ")
print()    
myList2.sort()
for v in myList2:
    print(v,end = " ")
