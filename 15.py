class Solution:
    def threeSum(self, nums: list):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        nums.sort()
        last = None
        for i in range(0, len(nums) - 2):
            low = i + 1
            high = len(nums) - 1
            if last == nums[i]:
                continue
            while low < high:
                if nums[low] + nums[high] + nums[i] == 0:
                    res.append([nums[low], nums[high], nums[i]])
                    while low < high and nums[low] == nums[low+1]:
                        low += 1
                    while low < high and nums[high] == nums[high-1]:
                        high -= 1
                    low += 1
                    high -= 1
                elif nums[low] + nums[high] + nums[i] > 0:
                    high -= 1
                else:
                    low += 1
            last = nums[i]
        return res


s = Solution()

print(s.threeSum([-1, 0, 1, 2, -1, -4]))