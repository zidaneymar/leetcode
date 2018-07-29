class Solution:
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        res = []
        nums = [i for i in range(1, n + 1)]
        def fill(nums: list, k, cur: list, index):
            if k - len(cur) > len(nums) - index:
                return
            if len(cur) == k:
                res.append(cur[:])
                return
            if index >= len(nums):
                return
            for i in range(index, len(nums)):
                cur.append(nums[i])
                fill(nums, k, cur, i + 1)
                cur.pop()
        fill(nums, k, [], 0)
        return res

x = Solution()

print (x.combine(4,3))