class list_node:
    def __init__(self):
        self.val=0
        self.next=None

head=[list_node()]*9                            #宣告一個節點型態陣列

data=[[1,2],[2,1],[1,3],[3,1],                  #圖形邊線陣列宣告 
      [2,4],[4,2],[2,5],[5,2],
      [3,6],[6,3],[3,7],[7,3],
      [4,8],[8,4],[5,8],[8,5],
      [6,8],[8,6],[8,7],[7,8]]

for i in range(1,9):
    head[i] = list_node()
    head[i].val = i
    head[i].next = None
    ptr = head[i]
    for j in range(len(data)):
        if data[j][0] == i:
            newnode =list_node()
            newnode.val = data[j][1]
            newnode.next = None
            while ptr.next:
                ptr = ptr.next
            ptr.next = newnode    

run=[0]*9
print('圖形的鄰接串列內容:')                    #列印圖形的鄰接串列內容            
for j in range(1,9):
    run[i]=0                                    #設定所有頂點成尚未走訪過
    print('頂點 %d =>' %head[j].val,end='')
    ptr=head[j]
    while ptr.next:
        ptr = ptr.next
        print(f"[{ptr.val}]",end="")
    print()
def dfs(current):
    run[current] = 1
    print(f"[{current}]",end="")
    ptr = head[current].next
    while ptr!= None:
        if run[ptr.val] == 0:
            dfs(ptr.val)
        ptr = ptr.next    
dfs(1)
print()
