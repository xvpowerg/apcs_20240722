#建立一個Circle 類 給予半徑r
#希望計算圓面積area
class Circle:
    def __init__(self,r):
        self.r = r
    def area(self):
        result = 3.1415 * self.r ** 2
        return result
c1 = Circle(10)
print(f"area:{c1.area():.2f}")
print(c1)    
