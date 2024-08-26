array1 = []
array1.append([5,6,7])
array1.append([7,8,9])
print(array1)

#10x5
p = [['']*5 for i in range(10)]
print(p)

for i in range(10):
    for j in range(5):
        p[i][j] = f"({i},{j})"

for v1 in p:
    for v in v1:
        print(v,end = " ")
    print()    
