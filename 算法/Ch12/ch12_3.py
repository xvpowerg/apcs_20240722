treasures = [50,160,20,100,20,60,90,120,150,30]
treasures.sort()
shipLoad = []
capcity = 500
total = 0
for treasure in treasures:
    if total + treasure < capcity:
       shipLoad.append(treasure)     
       total += treasure
    else:
        break
print(f"總重量:{total}公斤")
print(f"寶物數量{len(shipLoad)} 那些寶物{shipLoad}")
