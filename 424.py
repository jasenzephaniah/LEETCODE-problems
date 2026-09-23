class Solution(object):
    def characterReplacement(self, s, k):
        count = {}
        left = 0
        ml = 0
        r = 0
        for right in range(len(s)):
            count[s[right]] = count.get(s[right], 0) + 1
            ml = max(ml, count[s[right]])
            while (right - left + 1) - ml > k:
                count[s[left]] -= 1
                left += 1
            r = max(r, right - left + 1)
        return r
