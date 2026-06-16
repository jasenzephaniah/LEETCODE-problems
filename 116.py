class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return root
        queue = [root]
        while queue:
            level = []
            prev = None
            for _ in range(len(queue)):
                node = queue.pop(0)
                if prev:
                    prev.next = node
                prev = node
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return root
