for i in range(5):
    for k in range(4-i):
        print(" ",end = "")
    for x in range(2 * i + 1):
        print(chr(i + 65),end = "")
    print()    
