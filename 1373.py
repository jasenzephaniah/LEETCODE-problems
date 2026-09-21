class Solution(object):
    def maxSumBST(self, root):
        self.ans = 0
        INF = float('inf')
        def dfs(node):
            if not node:
                return (True, INF, -INF, 0)
            lb, lmin, lmax, lsum = dfs(node.left)
            rb, rmin, rmax, rsum = dfs(node.right)
            if lb and rb and lmax < node.val < rmin:
                total = lsum + rsum + node.val
                self.ans = max(self.ans, total)
                return (True, min(lmin, node.val), max(rmax, node.val), total)
            return (False, -INF, INF, 0)
        dfs(root)
        return self.ans
        
