def test(n):
    print("Start:",n)
    if n <=3:
        print(n)
        test(n + 1)      
    print("End:",n)

for i in range(1,4):
    print(i,end=" ")

print("")
test(1)
