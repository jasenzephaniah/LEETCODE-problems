class Solution(object):
    def findDegrees(self, matrix):
        ans = []
        for i in range(len(matrix)):
            ans.append(sum(matrix[i]))
        return ans
