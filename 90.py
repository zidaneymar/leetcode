class Solution:
    def subsetsWithDup(self, nums: list):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        nums.sort()

        temp = []

        i = 0
        cur = []
        while i < len(nums):
            if i < len(nums) - 1 and nums[i + 1] == nums[i]:
                cur.append(nums[i])
                i += 1
            
            if i == len(nums) - 1 or nums[i + 1] != nums[i]:
                cur.append(nums[i])
                temp.append(cur)
                cur = []
                i += 1
        def subsets(temp: list):    
            if len(temp) == 0:
                return [[]]
            theLastElement = temp.pop()
            # if len(temp) == 0 and len(theLastElement) == 1:
            #     return [[], theLastElement]

            res = []
            for element in subsets(temp[:]):
                res.append([] + element)
                for i in range(0, len(theLastElement)):
                    res.append([int(theLastElement[0])] * (i + 1) + element)
            return res

        return subsets(temp)


x = Solution()

print(x.subsetsWithDup([1,1]))