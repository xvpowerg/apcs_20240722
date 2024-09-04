import random

def guessCheck(gus,low,high):
     global answer
     if answer == gus:
         print("猜對了")
         return
     elif answer > gus:
           low =  gus + 1
     else:
           high = gus - 1
     guess = int(input(f"猜一個{low}~{high}整數"))
     guessCheck(guess,low,high)
     
start ,end = 1,100
answer = random.randint(start,end)
guess = int(input(f"猜一個{start}~{end}整數"))
guessCheck(guess,start,end)
