class Solution:
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        dp =  [0] * (len(s) + 1)
        dp[0] = 1

        for i in range(1, len(s) + 1):
            if int(s[i - 1]) >= 1 and int(s[i - 1]) <= 9:
                dp[i] += dp[i - 1]
            if i >= 2 and int(s[i - 2: i]) >= 10 and int(s[i - 2: i]) <= 26:
                dp[i] += dp[i - 2]
        return dp[len(s)]

x = Solution()
print(x.numDecodings("225"))