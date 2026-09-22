class Solution(object):
    def leastInterval(self, tasks, n):
        freq = {}
        for t in tasks:
            freq[t] = freq.get(t, 0) + 1
        maxFreq = max(freq.values())
        maxCount = sum(1 for v in freq.values() if v == maxFreq)
        frame = (maxFreq - 1) * (n + 1) + maxCount
        return max(len(tasks), frame)
