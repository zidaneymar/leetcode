class Solution:
    def findPairs(self, nums, k):
        res = set()
        buff = set()
        if k < 0:
            return 0
        for i in nums:
            
            if k + i not in buff and i - k not in buff:
                pass
            elif k + i in buff:
                if ((i, k + i) not in res) and ((k + i, i) not in res):
                    res.add((i, k + i))
            elif i - k in buff:
                if ((i, i - k) not in res) and ((i - k, i) not in res):
                    res.add((i, i - k))
            buff.add(i)
        
        return len(res)
            
        
            
            
        
print(Solution().findPairs([0,0,1,0,0],
1))