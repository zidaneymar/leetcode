# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def dfs(self, root):
        if not root:
            return
        
        self.dfs(root.left)
        self.buf.append(root.val)
        self.dfs(root.right)
        
        
        
        
    def findTarget(self, root: TreeNode, k: int) -> bool:
        self.buf = []
        
        self.dfs(root)

        l = 0
        r = len(self.buf) - 1
        
        while l < r:
            if self.buf[l] + self.buf[r] > k:
                r -= 1
            elif self.buf[l] + self.buf[r] < k:
                l += 1
            else:
                return True
        return False

