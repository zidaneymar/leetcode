class Solution:
    def largestDivisibleSubset(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        dp = [0] * len(nums)
        parent = [-1] * len(nums)
        
        maxRes = -1
        maxIndex = -1
        nums.sort()
        
        for i in range(0, len(nums)):
            if dp[i] == 0:
                dp[i] = 1
                if dp[i] > maxRes:
                    maxIndex = i
                    
            for k in range(0, i):
                # how to ensure the 
                if nums[i] % nums[k] == 0:
                    if dp[i] < dp[k] + 1:
                        dp[i] = dp[k] + 1
                        parent[i] = k
                        if dp[i] > maxRes:
                            maxIndex = i
        
        res = []
        cur = maxIndex
        while cur != -1:
            res.append(nums[cur])
            cur = parent[cur]
            
        res = res[::-1]
        return res

print(Solution().largestDivisibleSubset([2,3,4,9,8]))