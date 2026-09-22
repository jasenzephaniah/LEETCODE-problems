class Solution(object):
    def dailyTemperatures(self, temperatures):
        n = len(temperatures)
        r = [0] * n
        s = []
        for i in range(n):
            while s and temperatures[i] > temperatures[s[-1]]:
                k = s.pop()
                r[k] = i - k
            s.append(i)
        return r
