class Solution:
    def strangePrinter(self, s: str) -> int:
        
        if len(s) == 0:
            return 0
        
        dp = [[float('inf') for _ in range(len(s))] for _ in range(len(s))]
        
        for i in range(len(s)):
            dp[i][i] = 1
        
        for l in range(1, len(s)):
            for i in range(0, len(s)):
                if i + l < len(s):
                    if l == 1:
                        dp[i][i + l] = dp[i][i + l - 1] + 0 if s[i + l] == s[i] else 1 
                    else:
                        dp[i][i + l] = dp[i][i + l - 1] + 1
                        for k in range(i + 1, i + l):
                            dp[i][i + l] = min(dp[i][i + l], (dp[i][k] + dp[k + 1][i + l] - 1) if s[k] == s[i + l] else float('inf'))
                    
        return dp[0][-1]
                    
        
print(Solution().strangePrinter("aba"))