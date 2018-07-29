class Solution:
    def subsets(self, nums: list):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        res = []

        def subset(nums: list):
            res = [[]]
            temp = nums[:]
            if len(temp) == 0:
                return res
            cur = temp.pop() # which is 3
            subs = subset(temp) # all subsets of [1,2]
            for sub in subs:
                if sub != []:
                    res.append([] + sub)
                res.append([cur] + sub)
            return res
        res = subset(nums)
        return res

x = Solution()

print(x.subsets([1,2,3,4,5]))