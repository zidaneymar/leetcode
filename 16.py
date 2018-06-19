class Solution:
    def threeSumClosest(self, nums: list, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        res = []
        nums.sort()
        last = None
        closest = float("inf")
        for i in range(0, len(nums) - 2):
            low = i + 1
            high = len(nums) - 1
            if last == nums[i]:
                continue
            while low < high:
                if abs(nums[low] + nums[high] + nums[i] - target) < closest:
                    res = [nums[low], nums[high], nums[i]]
                    closest = abs(nums[low] + nums[high] + nums[i] - target)
                if nums[low] + nums[high] + nums[i] < target:
                    low += 1
                elif nums[low] + nums[high] + nums[i] > target:
                    high -= 1
                else:
                    return target
            last = nums[i]
        
        resNum = 0
        for num in res:
            resNum += num
        return resNum

s = Solution()

print(s.threeSumClosest([-1, 2, 1, -4], 1))