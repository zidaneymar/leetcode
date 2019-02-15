class Solution:
    def canIWin(self, maxChoosableInteger, desiredTotal):
        """
        :type maxChoosableInteger: int
        :type desiredTotal: int
        :rtype: bool
        """
        mem = {}
        if desiredTotal <= 0:
            return True
        chooseList = [False for i in range(0, maxChoosableInteger)]
        def dfs(chooseList, curTotal):
            
            for i in reversed(range(0, len(chooseList))):
                if not chooseList[i] and i + 1 >= curTotal:
                    return True


            
            if tuple(chooseList) in mem:
                return mem[tuple(chooseList)]
            
            for i in range(0, len(chooseList)):
                if not chooseList[i]:
                    chooseList[i] = True
                    if not dfs(chooseList, curTotal - i - 1):
                        mem[tuple(chooseList)] = True
                        chooseList[i] = False
                        return True
            mem[tuple(chooseList)] = False
            chooseList[i] = False
            return False
        
        return dfs(chooseList, desiredTotal)
                    
x = Solution()
print(x.canIWin(10, 11))