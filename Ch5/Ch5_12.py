subjs = ['國語', '數學', '英文']
scores = [100, 80, 95]
zipObj = zip(subjs,scores)
#print(list(zipObj))
for n,s in zipObj:
    print(n,s)
