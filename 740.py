class Solution(object):
    def deleteAndEarn(self, nums):
        m = max(nums)
        p = [0] * (m + 1)
        for x in nums:
            p[x] += x
        dp = [0] * (m + 1)
        dp[0] = 0
        if m >= 1:
            dp[1] = p[1]
        for i in range(2, m + 1):
            dp[i] = max(dp[i - 1], dp[i - 2] + p[i])
        return dp[m]
