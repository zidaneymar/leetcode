class Solution:
    def lcs(self, s1, s2):
        
        dp = [[0 for j in range(len(s2))] for i in range(len(s1))]
        
        for i, c1 in enumerate(s1):
            for j, c2 in enumerate(s2):
                if c1 == c2:
                    if i > 0 and j > 0:
                        dp[i][j] = dp[i - 1][j - 1] + 1
                    else:
                        dp[i][j] = 1
                else:
                    if i > 0 and j > 0:
                        dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
                    elif i > 0:
                        dp[i][j] = dp[i - 1][j]
                    elif j > 0:
                        dp[i][j] = dp[i][j - 1]

        return dp[-1][-1]

    def longestPalindromeSubseq(self, s: str) -> int:
        
        
        return self.lcs(s, s[::-1])
        
print(Solution().longestPalindromeSubseq('bbbab'))