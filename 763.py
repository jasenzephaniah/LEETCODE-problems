class Solution(object):
    def partitionLabels(self, s):
        l = {}
        for i in range(len(s)):
            l[s[i]] = i
        a, e = 0, 0
        p = []
        for i in range(len(s)):
            e = max(e, l[s[i]])
            if i == e:
                p.append(e - a + 1)
                a = i + 1
        return p
