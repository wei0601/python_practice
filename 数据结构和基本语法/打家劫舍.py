def rob(nums):
    sum = [0]*len(nums)
    if len(nums) == 0:
        return 0
    elif len(nums) == 1:
        return nums [0]
    elif len(nums) == 2:
        return max(nums[0], nums[1])
    else:
        sum[0] = nums[0]
        sum[1] = max(nums[0], nums[1])
        for i in range(2,len(nums)):
            sum[i] = max(sum[i-1],sum[i-2]+nums[i])
        return sum[len(nums)-1]
print(rob([2, 7, 9, 3, 1]))  # 12
print(rob([1, 2, 3, 1]))      # 4
print(rob([2, 1, 1, 2]))      # 4