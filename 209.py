class Solution:
    
    def upperBound(self, begin, end, nums, target):
        
        while begin < end:
            mid = begin + (end - begin) // 2
            if nums[mid] <= target:
                begin = mid + 1
            else:
                end = mid
                
        return begin
    
    
    def minSubArrayLen(self, s: int, nums) -> int:
        
        if sum(nums) < s:
            return 0
        preSum = [0] * len(nums)
        cur = 0
        res = float('inf')
        for i, n in enumerate(nums):
            cur += n
            preSum[i] = cur
            index = self.upperBound(0, i, preSum, preSum[i] - s) - 1
            if index in range(0, i + 1):
                res = min(res, i - index)
        return res
        
        
print(Solution().minSubArrayLen(7,
[2,3,1,2,4,3]))