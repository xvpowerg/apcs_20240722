a1,a2 = 1,3
print(a1,a2,sep="\t",end="\t")
for i in range(3,8):
   a3 = 3 * a2 - 2 * a1
   print(a3,end="\t")
   a1 = a2
   a2 = a3
   
