class Solution:
    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        
        dp = [[0 for _ in range(0, 2020)] for _ in range(0, len(nums))]
        
        for i in range(0, len(nums)):
            for j in range(0, 2020):
                if i > 0:
                    if j + nums[i] < 2020:
                        dp[i][j] += dp[i - 1][j + nums[i]]
                    if j - nums[i] >= 0:
                        dp[i][j] += dp[i - 1][j - nums[i]]
            
        return dp[-1][S + 1000]
    
print(Solution().findTargetSumWays([1,1,1,1,1], 3))