class Solution(object):
    def reverseWords(self, s):
        w = s.split()
        rw = w[::-1]
        return " ".join(rw)
