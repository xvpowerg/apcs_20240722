class list_node:
    def __init__(self):
        self.val = 0
        self.next = None
head = [list_node()] * 6

data=[[1,2],[2,1],[2,5],[5,2],                      #圖形陣列宣告
      [2,3],[3,2],[2,4],[4,2],
      [3,4],[4,3],[3,5],[5,3],
      [4,5],[5,4]]

for i in range(1,6):
    head[i] = list_node()
    head[i].val = i
    head[i].next = None
    print(f"頂點{i}",end="")
    ptr = head[i]
    for j in range(len(data)):
        if data[j][0] == i:
            newnode = list_node()
            newnode.val = data[j][1]
            newnode.next = None
            print(f"[{newnode.val}]",end="")
    print()     
