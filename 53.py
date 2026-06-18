class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cs = nums[0]
        ms = nums[0]
        for i in range(1, len(nums)):
            cs = max(cs + nums[i],nums[i])
            ms = max(ms,cs)
        return ms
