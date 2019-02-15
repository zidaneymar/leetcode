class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        def dfs(preorder, inorder):
            if len(inorder) == 0:
                return None
            curRoot = preorder.pop(0)
            newRootNode = TreeNode(curRoot)
            rootIndex = inorder.index(curRoot)
            newRootNode.left = dfs(preorder, inorder[:rootIndex])
            newRootNode.right = dfs(preorder, inorder[rootIndex + 1:])
            return newRootNode
    
        return dfs(preorder, inorder)


x = Solution().buildTree([3,9,20,15,7], [9,3,15,20,7])

print(x)