def f1(x):
    return x ** 2
print(f1(5))

f2 = lambda x : x ** 2
print(f2(5))


myMax = lambda x,y : x if x > y else y
print(myMax(10,5))
print(myMax(10,65))
