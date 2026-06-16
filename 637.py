class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
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
            res.append(sum(level) / len(level))
        return res
