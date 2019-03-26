import collections

class Solution(object):
    def check(self, c1, c2):
        for i in c1:
            if (c1[i] != 0 and i not in c2) or (i in c2 and c2[i] != c1[i]):
                return False
        return True
    
    
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        c = collections.Counter(p)
        
        cur = {}
        
        for i in range(0, len(p)):
            cur[s[i]] = cur[s[i]] + 1 if s[i] in cur else 1
        
        succ = True
        for i in range(0, len(p)):
            if cur[s[i]] != c[s[i]]:  
                succ = False
        
        res = set()
        if succ:
            res.add(0)
        
        for i in range(1, len(s) - len(p) + 1):
            cur[s[i - 1]] -= 1
            cur[s[i + len(p) - 1]] = cur[s[i + len(p) - 1]] + 1 if s[i + len(p) - 1] in cur else 1
            if cur[s[i - 1]] == c[s[i - 1]] and cur[s[i + len(p) - 1]] == c[s[i + len(p) - 1]] and i - 1 in res:
                res.add(i)
                continue
            if self.check(cur, c):
                res.add(i)
                
        
        return list(res)


print(Solution().findAnagrams("cbaebabacd",
"abc"))