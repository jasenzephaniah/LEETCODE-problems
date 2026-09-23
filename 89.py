class Solution(object):
    def grayCode(self, n):
        t = 1 << n
        return [i ^ (i >> 1) for i in range(t)]
