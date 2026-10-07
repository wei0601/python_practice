def next_large_number(nums):
    if not nums:
        return None
    n = len(nums)
    result = [-1]*n
    for i in range(n):
        for j in range(i + 1, n):
            if nums[j] > nums[i]:
                result[i] = nums[j]
                break
    
    return result 
#######################################上面的版本时间复杂度太高啦，这道题目可以采用单调栈优化
def next_large_number_optimized(nums):
    if not nums:
        return None
    n = len(nums)
    result = [-1]*n
    stack = []
    for i in range(n-1,-1,-1):
        while stack and nums[i] >= stack[-1]:
            stack.pop()
        if stack:
            result[i] = stack[-1]
        stack.append(nums[i])
    return result