#p1 來源
#p2 中繼
#p3 目標
def hanoi(n,p1,p2,p3):
    if n == 1:
        print(f"{n}套環從{p1}移動到{p3}")
    else:
       hanoi(n-1,p1,p3,p2)
       print(f"{n}套環從{p1}移動{p3}")
       hanoi(n-1,p2,p1,p3)
i = int(input("請輸入套環數量:"))
hanoi(i,"A","B","C")
