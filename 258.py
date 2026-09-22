class Solution(object):
    def addDigits(self, num):
        while num >= 10:
            t = 0
            while num > 0:
                t += num % 10
                num //= 10
            num = t
        return num
