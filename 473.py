class Solution(object):
    def makesquare(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        nums.sort(reverse=True)
        allSum = sum(nums)
        if allSum % 4 != 0:
            return False
        target = int(allSum / 4)
        
        def dfs(sumList, target, i):
            
            if i == len(nums):
                if (sumList[0] == target and sumList[1] == target and sumList[2] == target and sumList[3] == target):
                    return True
                return False
            for j in range(0, 4):
                if nums[i] + sumList[j] <= target:
                    sumList[j] += nums[i]
                    if dfs(sumList, target, i + 1):
                        return True
                    sumList[j] -= nums[i]
            return False
            
        return dfs([0, 0, 0, 0], target, 0)

print(Solution().makesquare([5,5,5,5,4,4,4,4,3,3,3,3]))