class Solution(object):
    def minCapability(self, nums, k):
        def count_robbable(cap):
            count = 0
            i = 0
            n = len(nums)
            while i < n:
                if nums[i] <= cap:
                    count += 1
                    i += 2  
                else:
                    i += 1
            return count
        lo, hi = min(nums), max(nums)
        while lo < hi:
            mid = (lo + hi) // 2
            if count_robbable(mid) >= k:
                hi = mid
            else:
                lo = mid + 1
        return lo
