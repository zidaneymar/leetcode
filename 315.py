class Solution:
    def lowerBound(self, nums, begin, end, target):

        while begin < end:
            mid = begin + (end - begin) // 2
            if nums[mid] < target:
                begin = mid + 1
            else:
                end = mid
        return begin
    
    def insert(self, nums, start):
        while start + 1 < len(nums) and nums[start] > nums[start + 1]:
            nums[start + 1], nums[start] = nums[start], nums[start + 1]
            start += 1

    def countSmaller(self, nums):
        res = [None] * len(nums)
        for i in reversed(range(0, len(nums))):
            number = self.lowerBound(nums, i + 1, len(nums), nums[i])
            res[i] = number - i - 1
            buf = nums[i]
            nums = nums[:i] + nums[i + 1:]
            nums.insert(number - 1, buf)
        return res
print(Solution().countSmaller([5,2,6,1]))