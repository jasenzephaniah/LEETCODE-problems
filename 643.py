class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        n = len(nums)
        s = sum(nums[:k])
        ma = s
        for i in range(k,n):
            s += nums[i] - nums[i - k]
            ma = max(ma,s)
        return ma/k
