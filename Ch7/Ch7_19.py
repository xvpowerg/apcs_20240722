num1 = 10
num2 = 0
nums = [1,3,5,7,9]
try:
     print(num1 / num2)
     print(nums[99])
except ZeroDivisionError:
    print("分母不可為0")
except IndexError:
     print("Index錯誤")
