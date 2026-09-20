class Solution(object):
    def reverse(self, x):
        s = -1 if x < 0 else 1
        x = abs(x)
        rev = 0
        while x > 0:
            d = x % 10
            rev = rev * 10 + d
            x //= 10
        rev *= s
        if rev < -2 ** 31 or rev > 2 ** 31 - 1:
            return 0
        return rev
