class Solution:
    def canJump(self, nums: list):
        """
        :type nums: List[int]
        :rtype: bool
        """
        reachable = [False] * len(nums)
        reachable[0] = True
        for i in range(1, len(nums)):
            for j in reversed(range(0, i)):
                if reachable[j] and j + nums[j] >= i:
                    reachable[i] = True
                    break

        return reachable[len(nums) - 1]

x = Solution()
print(x.canJump([2,3,1,1,4]))