class Solution:
    def permuteUnique(self, nums: list):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result_set = set()
        
        def dfs(index, curRes: list):
            if index >= len(curRes):
                result_set.add(tuple(curRes))
            for i in range(index, len(curRes)):
                curRes[index], curRes[i] = curRes[i], curRes[index]
                dfs(index + 1, curRes)
                curRes[index], curRes[i] = curRes[i], curRes[index]

        dfs(0, nums)
        result = []
        for tuples in result_set:
            result.append(list(tuples))
        return result
x = Solution()

print(x.permuteUnique([1,1,2]))