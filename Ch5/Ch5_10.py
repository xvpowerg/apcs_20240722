c = 65
for i in range(0,6):
    for j in range(0,6):
        if j <=i:
            continue
        for k in range(0,6):
            if k <= j:
                continue
            print(f"{chr(c+i)}{chr(c+j)}{chr(c+k)}")
            
