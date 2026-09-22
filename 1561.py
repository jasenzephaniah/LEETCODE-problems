class Solution(object):
    def maxCoins(self, piles):
        piles.sort()
        n = len(piles) // 3
        return sum(piles[n::2])
