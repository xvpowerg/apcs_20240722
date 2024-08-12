import random
def myChoice(data):     
    indx = random.randint(1,len(data)) -1
    return fruits[indx]

fruits = ["香蕉","蘋果","橘子","西瓜"]
f = myChoice(fruits)
print(f)
