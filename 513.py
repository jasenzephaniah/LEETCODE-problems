class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        res = []
        if not root:
            return []
        queue = [root]
        while queue:
            level = []
            for _ in range(len(queue)):
                node = queue.pop(0)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                level.append(node.val)
            res.append(level)
        return res[-1][0]
