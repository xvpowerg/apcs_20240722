a = [60,70,75,90,100]
b = a
print(a)
print(b)
print("="*50)
b[1] = 88
print(a)
print(b)
print("="*50)
print("======測試Copy===========")
a = [60,70,75,90,100]
b = a[:]
print(a)
print(b)
print("="*50)
b[1] = 88
print(a)
print(b)
print("="*50)
