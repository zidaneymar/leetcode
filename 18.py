class Solution:
    def fourSum(self, nums: list, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        
        """

        def threeSum(nums: list, target):
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
                    if nums[low] + nums[high] + nums[i] == target:
                        res.append([nums[low], nums[high], nums[i]])
                        while low < high and nums[low] == nums[low+1]:
                            low += 1
                        while low < high and nums[high] == nums[high-1]:
                            high -= 1
                        low += 1
                        high -= 1
                    elif nums[low] + nums[high] + nums[i] > target:
                        high -= 1
                    else:
                        low += 1
                last = nums[i]
            return res
        i = 0
        res = []
        nums.sort()
        while i < len(nums):
            num = nums[i]
            new_target = target - num
            new_nums = nums[i + 1:]
            new_list = threeSum(new_nums, new_target)
            if new_list and new_list != []:
                for each_list in new_list:
                    each_list.append(num)
                    res.append(each_list)
                while i + 1 < len(nums) and nums[i+1] == nums[i]:
                    i += 1
            i += 1
        return res
        
s = Solution()
print(s.fourSum([-1,-5,-5,-3,2,5,0,4], -7))