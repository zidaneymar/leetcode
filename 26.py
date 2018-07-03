class Solution:
    def removeDuplicates(self, nums: list):
        """
        :type nums: List[int]
        :rtype: int
        """
        def binaryRemove(nums: list, left, right):
            if left >= right:
                return 0
            if left == right - 1:
                if nums[left] == nums[right]:
                    del nums[left]
                    return 1
                else:
                    return 0
            if nums[left] == nums[right]:
                del nums[left:right]
                return right - left
            mid = (left + right) // 2
            return binaryRemove(nums, mid, right) + binaryRemove(nums, left, mid)
        length = len(nums)
        return length - binaryRemove(nums, 0, len(nums) - 1)
    


x = Solution()
print(x.removeDuplicates([1,1,1,2,3,4,5,5,6]))