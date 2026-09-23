class Solution(object):
    def longestBeautifulSubstring(self, word):
        n = len(word)
        if n < 5:
            return 0
        a = 0
        c = 1
        s = 0
        for i in range(1, n):
            if word[i] > word[i - 1]:
                c += 1
            elif word[i] < word[i - 1]:
                c = 1
                s = i
            if c == 5:
                a = max(a, i - s + 1)
        return a
