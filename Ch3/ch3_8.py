scroes = [60,70,75,90,100]
print(scroes[3])
print(scroes[-2])
print("="*50)
for v in scroes:
    print(v,end=" ")
print()    
print("="*50)
del scroes[1]
print(scroes)
print("="*50)

del scroes[1:3]
print(scroes)
print("="*50)

del scroes
print(scroes)
print("="*50)
