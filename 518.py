class Solution:
    def change(self, amount: int, coins) -> int:
        
        dp = [[0 for i in range(amount + 1)] for j in range(len(coins))]        
        
        
        dp[0][0] = 1
        
        for i in range(len(coins)):
            dp[i][0] = 1
            for j in range(1, amount + 1):
                dp[i][j] = (dp[i][j - coins[i]] if j >= coins[i] else 0) + (dp[i - 1][j] if i >= 1 else 0)
        
        return dp[-1][-1]

print(Solution().change(5, [1,2,5]))