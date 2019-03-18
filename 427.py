class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight

class Solution:
    def dfs(self, g, x, y, h):
        if h == 1:
            val = None
            if g[x][y] == 1:
                val = True
            else:
                val = False
            
            return Node(val, True, None, None, None, None)
        
        r1 = self.dfs(g, x, y, h // 2)
        r2 = self.dfs(g, x + h // 2, y, h // 2)
        r3 = self.dfs(g, x, y + h // 2, h // 2)
        r4 = self.dfs(g, x + h // 2, y + h // 2, h // 2)
        
        if r1.val == r2.val == r3.val == r4.val:
            return Node(r1.val, True, None, None, None, None)
        return Node(None, False, r1, r3, r2, r4)
        
        
    def construct(self, grid) -> 'Node':
        return self.dfs(grid, 0, 0, len(grid))

a = Solution().construct([[1,1,0,0,0,0,0,0],[1,1,0,0,0,0,0,0],[1,1,0,0,0,0,1,1],[1,1,0,0,0,0,1,1],[0,0,0,0,0,0,1,1],[0,0,0,0,0,0,1,1],[1,1,1,1,1,1,0,0],[1,1,1,1,1,1,0,0]])
print(a)