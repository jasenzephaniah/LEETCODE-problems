class Solution(object):
    def decodeString(self, s):
        n = []
        ss = []
        num = 0
        c = ""
        for ch in s:
            if ch.isdigit():
                num = num * 10 + int(ch)
            elif ch == '[':
                n.append(num)
                ss.append(c)
                num = 0
                c = ""
            elif ch == ']':
                c = ss.pop() + c * n.pop()
            else:
                c += ch
        return c
