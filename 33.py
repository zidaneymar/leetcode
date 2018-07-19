class Solution:
    def search(self, nums: list, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int

        """
        def search_index(nums: list, low: int, high: int):
            if len(nums) == 0:
                return -1
            mid = (int)((low + high) / 2)
            if nums[mid] == target:
                return mid
            if (high - low) <= 0:
                return -1
            if nums[mid] <= nums[high]:
                if target > nums[mid] and target <= nums[high]:
                    return search_index(nums, mid + 1, high)
                else:
                    return search_index(nums, low, mid - 1)
            if nums[mid] >= nums[low]:
                if target >= nums[low] and target < nums[mid]:
                    return search_index(nums, low, mid - 1)
                else:
                    return search_index(nums, mid + 1, high)

        low = 0
        high = len(nums) - 1
        return search_index(nums, low, high)


x = Solution()
print(x.search([3,1], 0))

