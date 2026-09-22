class Solution(object):
    def removeKdigits(self, num, k):
        s = []
        for d in num:
            while k > 0 and s and s[-1] > d:
                s.pop()
                k -= 1
            s.append(d)
        while k > 0:
            s.pop()
            k -= 1
        r = "".join(s).lstrip('0')
        return r if r else "0"
        
