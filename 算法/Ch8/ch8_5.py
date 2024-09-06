def showData(data_list):
    for i in range(len(data_list)):
        print(f"{data_list[i]}",end=" ")
    print()    
class Student:
    def __init__(self,name,age,gpa):
        self.name = name
        self.age = age
        self.gpa = gpa
    def __lt__(self,other):
        return self.age < other.age
    def __str__(self):
        return f"{self.name}:{self.age}:{self.gpa}"
data = [Student("Amy",15,4.2),
        Student("Bill",16,3.8),
        Student("Chris",13,4.0),
        Student("David",19,4.8),
        Student("Ed",17,2.6)]    
showData(sorted(data) )
#print(data[0] < data[1])
n = len(data)
for i in range(n-1):
    minIdx = i
    for j in range(i+1,n):
        if data[j] < data[minIdx]:
            minIdx = j
    data[i],data[minIdx] = data[minIdx],data[i]

showData(data)
