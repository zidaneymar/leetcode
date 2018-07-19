class Solution:
    def searchRange(self, nums: list, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        def binarySearch(nums: list, target, low, high):
            if len(nums) == 0:
                return -1
            mid = (int)((low + high) / 2)
            if nums[mid] == target:
                return mid
            if high - low <= 0:
                return -1
            if nums[mid] > target:
                return binarySearch(nums, target, low, mid - 1)
            else:
                return binarySearch(nums, target, mid + 1, high)
        
        index = binarySearch(nums, target, 0, len(nums) - 1)
        if index == -1:
            return [-1, -1]
        low_index = index
        high_index = index

        while low_index - 1 >= 0 and nums[low_index - 1] == nums[low_index]:
            low_index -= 1
        while high_index + 1 < len(nums) and nums[high_index + 1] == nums[high_index]:
            high_index += 1
        return [low_index, high_index]


x = Solution()
print(x.searchRange([1], 1))