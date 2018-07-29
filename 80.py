class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        curNum = 0
        prev = None
        i = 0
        while i < len(nums):
            if prev == None:
                prev = nums[i]
                i += 1
            else:
                if prev == nums[i]:
                    curNum += 1
                    if curNum >= 2:
                        prev = nums[i]
                        del nums[i]
                        i -= 1
                    else:
                        prev = nums[i]
                else:
                    curNum = 0
                    prev = nums[i]
                i += 1
        return len(nums)
    
x = Solution()

test = [0,0,0,0,0]
print(x.removeDuplicates(test))
print(test)