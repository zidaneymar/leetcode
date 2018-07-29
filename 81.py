class Solution:
    def search(self, nums: list, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        
        
        low = 0
        high = len(nums) - 1
        
        while low <= high:
            mid = int((low + high) / 2)
            if nums[mid] == target:
                return True
            if nums[mid] < nums[high]: # the right part is ascending 
                if target > nums[mid] and target <= nums[high]:
                    low = mid + 1
                else:
                    high = mid - 1
            elif nums[low] < nums[mid]: # the left part is ascending 
                if target < nums[mid] and target >= nums[low]:
                    high = mid - 1
                else:
                    low = mid + 1
            elif nums[mid] == nums[high] == nums[low]:
                high -= 1
                low += 1
            elif nums[mid] == nums[high]:
                if target == nums[mid]:
                    return True
                else:
                    high = mid - 1
            elif nums[mid] == nums[low]:
                if target == nums[mid]:
                    return True
                else:
                    low = mid + 1
        return False


x = Solution()
print(x.search([1,1,3,1], 3))