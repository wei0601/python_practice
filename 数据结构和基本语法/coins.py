def coins(coins, amount):
    nums = [-1]*(amount+1)
    nums[0] = 0
    for i in range(1, amount+1):
        for coin in coins:
            if i - coin >=0 and nums[i-coin] != -1:
                if nums[i] == -1:
                    nums[i] = nums[i-coin] + 1
                else:
                    nums[i] = min(nums[i], nums[i-coin]+1)
    return nums[amount]