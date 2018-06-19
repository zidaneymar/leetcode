class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        class Pattern:
            def __init__(self, token: str, iter: bool):
                self.token = token
                self.iter = iter

        def handlePattern(p: str) -> list:
            res = list()
            i = 0
            while i < len(p):
                if p[i] != '*' and i + 1 < len(p) and p[i+1] == '*':
                    res.append(Pattern(p[i], True))
                    i += 2
                else:
                    res.append(Pattern(p[i], False))
                    i += 1
            return res
        
        
        p = handlePattern(p)
        
        dp = [[False for x in range(len(p)+1)] for y in range(len(s)+1)]
        dp[0][0] = True
        for i in range(0, len(s)+1):
            for j in range(0, len(p)+1):
                if i == j == 0:
                    continue
                res1 = res2 = res3 = False
                if i > 0 and j > 0:
                    res1 = dp[i-1][j-1] and p[j-1].token in [s[i-1], "."]
                    res2 = dp[i-1][j] and p[j-1].token in [s[i-1], "."] and p[j-1].iter
                if j > 0:
                    res3 = dp[i][j-1] and p[j-1].iter
                dp[i][j] = res1 or res2 or res3

        return dp[len(s)][len(p)]
# Why increasing index could not handle the all paths
# Why increasing index should use dp(i, j) -> can't handle all pahts

# Why decreasing index can iterate all paths???? -> no way, it's the same
# 
# 
# DP has another way -> memorizing recursive 

x = Solution()
print(x.isMatch("aa", "aaa"))

   

    