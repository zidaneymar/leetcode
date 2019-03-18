class Solution:
    
    def isSub(self, str1, str2):
        
        i = 0
        
        for s in str1:
            if str2[i] == s:
                i += 1
            if i == len(str2):
                return True
        return False 
       
    
    def findLUSlength(self, strs) -> int:
        strs.sort(key = len, reverse = True)
        
        for i, s in enumerate(strs):
            res = True
            for j in range(0, i):
                if self.isSub(strs[j], s):
                    res = False
                    break
            if res and i > 0:
                return len(s)
        return -1

print(Solution().findLUSlength(["aabbcc", "aabbcc","cb","abc"]))