
nums = [4,5,0,0,0,7,2,34,0]

num = len(nums)
zero = 0
for i in range(num,0,-1):
    if nums[i] != 0:
        nums[i],nums[zero] = nums[zero],nums[i]
        zero += 1

print(nums)