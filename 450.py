class Solution(object):
    def min(self,root):
        current = root
        while current.left:
            current = current.left
        return current
    def deleteNode(self, root, key):
        if root is None:
            return None
        if key < root.val:
            root.left = self.deleteNode(root.left,key)
        elif key > root.val:
            root.right = self.deleteNode(root.right,key)
        else:
            if root.left is None:
                return root.right
            if root.right is None:
                return root.left
            t = self.min(root.right)
            root.val = t.val
            root.right = self.deleteNode(root.right,t.val)
        return root
