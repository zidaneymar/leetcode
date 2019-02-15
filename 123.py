
class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        
        dp = [[0 for _ in range(0, len(prices))] for _ in range(0, 3)]
        
        
        for k in range(1, 3):
            maxInJ = 0
            for i in range(0, len(prices)):
                maxInJ = max(maxInJ, dp[k - 1][i] + prices[i] - prices[j])
                if i > 0:
                    dp[k][i] = max(dp[k][i - 1], maxInJ)
        
        return max(dp[1][-1], dp[2][-1])
    

x = Solution()
print(x.maxProfit([1,2,3,4,5]))