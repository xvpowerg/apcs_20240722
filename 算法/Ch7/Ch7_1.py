H = int(input('輸入樹高: '))
D = int(input('白天上升公尺數: '))
N = int(input('晚上下降公尺數: '))

height = D
days = 1
while height < H:
    height -= N
    height += D
    days += 1

print(f'蝸牛第{days}天可爬到樹頂')
