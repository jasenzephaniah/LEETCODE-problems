class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        queue = [root]
        max_sum = float('-inf')
        ans = 1
        level_num = 1

        while queue:
            s = 0

            for _ in range(len(queue)):
                node = queue.pop(0)
                s += node.val

                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)

            if s > max_sum:
                max_sum = s
                ans = level_num

            level_num += 1

        return ans
