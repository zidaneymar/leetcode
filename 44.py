class Solution:
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        dp = [[False for i in range(0, len(p) + 1)] for j in range(0, len(s) + 1)]
        
        if len(s) == 0 or len(p) == 0:
            return False
        
        dp[0][0] = True
 
        for i in range(0, len(s) + 1):
            for j in range(1, len(p) + 1):
                if i > 0:
                    if p[j - 1] == '*':
                        dp[i][j] = dp[i - 1][j] or dp[i - 1][j - 1] or dp[i][j - 1]
                    elif p[j - 1] == '?':
                        dp[i][j] = dp[i - 1][j - 1]
                    else:
                        dp[i][j] = True if s[i - 1] == p[j - 1] and dp[i - 1][j - 1] else False
                else:
                    if p[j - 1] == '*':
                        dp[i][j] = True
              
        
        return dp[len(s)][len(p)]

x = Solution()
print(x.isMatch('aab', 'c*a*b'))