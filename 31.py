class Solution:
    def nextPermutation(self, nums: list):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        
        last = None
        for i in reversed(range(0, len(nums))):
            if not last:
                last = nums[i]
                continue
            cur = nums[i]
            if cur < last:
                index = None
                curMin = None
                for j in range(i + 1, len(nums)):
                    if nums[j] > cur:
                        if not curMin:
                            curMin = nums[j]
                            index = j
                        else:
                            if curMin >= nums[j]:
                                index = j
                                curMin = nums[j]                    
                nums[i], nums[index] = nums[index], nums[i]
                nums[i+1:] = nums[i+1:][::-1]
                return
            last = cur
        nums.reverse()
                    
    



x = Solution()
test = [5,4,3,2,1]
x.nextPermutation(test)
print(test)
        