class Point:
    def __init__(self,x = 0,y = 0):
        self.x = x
        self.y = y
    def __str__(self):
        return f"({self.x},{self.y})"
    def __add__(self,other):
        x = self.x + other.x
        y = self.y + other.y
        return Point(x,y)
#https://docs.python.org/3/library/operator.html
p1 = Point(2,3)
p2 = Point(-1,2)
print(p1 + p2)
