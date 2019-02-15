# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    prev = None
    def dfs(self, root):
        
        if not root:
            return None

        self.dfs(root.right)
        self.dfs(root.left)

        root.right = self.prev
        root.left = None
        self.prev = root
        
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        return self.dfs(root)

