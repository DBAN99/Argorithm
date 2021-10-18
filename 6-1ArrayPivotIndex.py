nums = [1,8,2,9,3,4,4]
total = sum(nums)

left_total = 0
if len(nums) == 0:
    print('-1')
if total - nums[0] == 0:
    print(0)

for i in range(1, len(nums) - 1):
    left_total += nums[i - 1]
    if left_total * 2 == total - nums[i]:
        print(i)


if total - nums[-1] == 0:
    print(len(nums) - 1)



