import random
nums = random.sample(range(1,100),10)


nums.sort()
print(nums)
print(nums[-3:])
maxSum =  sum(nums[-3:])
print(maxSum)
