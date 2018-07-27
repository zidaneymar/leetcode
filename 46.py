class Solution:
    def permute(self, nums: list):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []

        def dfs(index, curRes):
            if index >= len(curRes):
                res.append(curRes[:])
                return
            for i in range(index, len(nums)):
                curRes[i] , curRes[index] = curRes[index], curRes[i]
                dfs(index + 1, curRes)
                curRes[i] , curRes[index] = curRes[index], curRes[i]

        curRes = nums[:]
        dfs(0, curRes)
        return res
x = Solution()

print(x.permute([1,2,3]))