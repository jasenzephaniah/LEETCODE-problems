class Solution(object):
    def rangeBitwiseAnd(self, left, right):
        s = 0
        while left < right:
            left >>= 1
            right >>= 1
            s += 1
        return left << s
