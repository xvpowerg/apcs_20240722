import random
start,end = 1,100
answer  = random.randint(start,end)
guess = int(input(f"猜數字{start}~{end}:"))

while True:
    if guess == answer:
        print("猜對了")
        break
    elif guess > answer:
        end = guess - 1
    else:
        start = guess + 1
    guess = int(input(f"猜數字{start}~{end}:"))
    

