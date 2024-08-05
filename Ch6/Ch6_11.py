def sumFunc(n1,n2,*other):
    s = n1 + n2
    for i in other:
        s += i
    return s

print(sumFunc(1,2))
print(sumFunc(1,2,3,4,5))
