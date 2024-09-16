class Knapsack:
    def __init__(self,capacity): 
        self.capacity = capacity
        self.items = []
        self.weight = 0
        self.value = 0
    def put(self,item):    
            if self.weight + item.weight  > capacity:
                return False
            self.items.append(item)
            self.weight += item.weight
            self.value += item.value
            return True
    def print(self):
        print(f"Items:{''.join(map(str,self.items))}")
        print(f"Weight:{self.weight}")
        print(f"Value:{self.value}")
class Item:
    def __init__(self,weight,value):
        self.weight = weight
        self.value = value
        self.unitValue = self.value / self.weight
        
    def __lt__(self,other):
        return self.unitValue < other.unitValue
    def __str__(self):
        return f"({self.weight},{self.value})"
       
capacity = 5            
k = Knapsack(capacity)

weight = [1,2,3]
values = [20,60,45]
items = []
for w,v in zip(weight,values):
    items.append(Item(w,v))

items.sort(reverse=True)
for item in items:
    if not k.put(item):
        break
k.print()    
