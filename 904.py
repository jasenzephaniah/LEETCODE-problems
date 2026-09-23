class Solution(object):
    def totalFruit(self, fruits):
        n = len(fruits)
        c = {}
        l = 0
        ml = 0
        for r in range(n):
            c[fruits[r]] = c.get(fruits[r], 0) + 1
            while len(c) > 2:
                c[fruits[l]] -= 1
                if c[fruits[l]] == 0:
                    del c[fruits[l]]
                l += 1
            ml = max(ml, r - l + 1)
        return ml
