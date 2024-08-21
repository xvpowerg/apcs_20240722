y = 1
for i in range(5):
    for k in range(4-i):
        print(" ",end = "")
    for x in range(y):
        print(chr(i + 65),end = "")
    y += 2    
    print()    
