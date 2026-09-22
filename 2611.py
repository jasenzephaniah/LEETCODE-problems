class Solution(object):
    def miceAndCheese(self, reward1, reward2, k):
        n = len(reward1)
        d = sorted(reward1[i] - reward2[i] for i in range(n))
        b = sum(reward2)
        return b + sum(d[n - k:])
