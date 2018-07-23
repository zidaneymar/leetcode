class Solution:
    def combinationSum(self, candidates: list, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        result = []
        def dfs(candidates: list, target, curList, index, curSum):
            if curSum == target:
                result.append(curList)
                return
            if curSum > target or index >= len(candidates):
                return
            
            if curSum < target:
                newList = list(curList)
                newList.append(candidates[index])
                dfs(candidates, target, newList, index, curSum + candidates[index])
                dfs(candidates, target, curList, index + 1, curSum)
        
        curList = []
        dfs(candidates, target, curList, 0, 0)
        return result
    
x = Solution()

print(x.combinationSum([2,3,6,7], 7))