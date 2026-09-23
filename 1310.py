class Solution(object):
    def xorQueries(self, arr, queries):
        n = len(arr)
        p = [0] * (n + 1)
        for i in range(n):
            p[i + 1] = p[i] ^ arr[i]
        return [p[r + 1] ^ p[l] for l, r in queries]
