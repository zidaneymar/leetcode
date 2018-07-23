class Solution:
    def combinationSum2(self, candidates: list, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        result = set()
        def dfs(candidates: list, target, curList, curSum, index):
            if curSum == target:
                result.add(tuple(curList))
            if index >= len(candidates) or curSum > target:
                return
            
            dfs(candidates, target, curList, curSum, index + 1)

            newList = list(curList)
            newList.append(candidates[index])
            dfs(candidates, target, newList, curSum + candidates[index], index + 1)
        
        curList = []
        dfs(candidates, target, curList, 0, 0)
        
        resList = []
        for forset in result:
            resList.append(list(forset))
        return resList
    
x = Solution()
print(x.combinationSum2([10,1,2,7,6,1,5], 8))