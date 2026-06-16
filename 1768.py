class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        m = len(word1)
        n = len(word2)
        i = 0
        res = ''
        while i < m or i < n:
            if i < m:
                res += word1[i]
            if i < n:
                res += word2[i]
            i += 1
        return res
