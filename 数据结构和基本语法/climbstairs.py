def climbstairs(n):
    if n <=1:
        return 1
    result = climbstairs(n - 1) + climbstairs(n - 2)
    return result
##动态规划核心思想：把已经计算过的结果保存下来
def climbstairs_dp(n):
    if n <= 1:
        return 1
    dp = [0] * (n + 1)
    dp[0] = 1
    dp[1] = 1
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    return dp[n]
print(climbstairs_dp(4))