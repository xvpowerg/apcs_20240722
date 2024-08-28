scores = [[70,80,90],
         [60,55,70],
         [77,88,99]]
for c in range(len(scores[0])):
    for r in range(len(scores)):
        print(scores[r][c],end = " ")
    print()    
print()

for i in range(len(scores)):
    #print(i,"_",2-i)
    print(scores[i][2-i])
    

"""
02 11 20


00 01 02
10 11 12
20 21 22
"""
