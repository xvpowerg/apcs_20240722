def seqFunc(x):
    if x == 1:
        return 1
    elif x == 2:
        return 3
    else:
        return 3 * seqFunc(x - 1) -  2 * seqFunc(x - 2) 
for j in range(1,8):
    print(seqFunc(j),end="\t")
