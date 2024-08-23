for i in range(-4,5):
    for k in range(-4,5):
        if 4 - abs(k) > abs(i):
            print(" ",end = "")
        else:
            print("*",end="")
    print()    
    
