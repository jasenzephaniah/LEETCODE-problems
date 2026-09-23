class Solution(object):
    def subsets(self, nums):
        n = len(nums)
        r = []
        for i in range(1 << n):
            c = []
            for j in range(n):
                if i & (1 << j):
                    c.append(nums[j])
            r.append(c)
        return r
