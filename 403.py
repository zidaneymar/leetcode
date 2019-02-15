class Solution:
    def canCross(self, stones):
        """
        :type stones: List[int]
        :rtype: bool
        """
        
        mem = {}
        stonesSet = set(stones)
        
        def search(index, step):
            if (index, step) in mem:
                return mem[(index, step)]
            if index == 0:
                return index + 1 in stonesSet and search(index + 1, 1)
            if index == stones[-1]:
                return True
            res1 = False
            res2 = False
            res3 = False
            if (index + step - 1) in stonesSet and step != 1:
                res1 = search(index + step - 1, step - 1)
            if (index + step) in stonesSet and step != 0:
                res2 = search(index + step, step)
            if (index + step + 1) in stonesSet:
                res3 = search(index + step + 1, step + 1)
            
            mem[(index, step)] = res1 or res2 or res3
            return res1 or res2 or res3
    
        return search(0, 1)

x = Solution()
print(x.canCross([0, 2]))