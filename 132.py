class Solution:
    def minCut(self, s):
        """
        :type s: str
        :rtype: int
        """
        pal = [[False for i in range(0, len(s))] for j in range(0, len(s))]
        
        for i in reversed(range(0, len(s))):
            for j in range(i, len(s)):
                if i == j:
                    pal[i][j] = True
                elif j == i + 1:
                    if s[i] == s[j]:
                        pal[i][j] = True
                else:
                    if j - 1 >= i + 1 and s[i] == s[j] and pal[i + 1][j - 1]:
                        pal[i][j] = True
                
        cut = [float('inf')] * len(s)
        
        for i in range(0, len(s)):
            if pal[0][i]:
                cut[i] = 0
            else:
                for j in range(1, i + 1):
                    if pal[j][i]:
                        cut[i] = min(cut[i], cut[j - 1] + 1)
            
        
        return cut[len(s) - 1]
x = Solution()
print(x.minCut("abaccdefg"))