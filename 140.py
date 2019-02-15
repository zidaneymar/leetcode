class Solution:
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
       
        wordSet = set(wordDict)
        
        mem = {}
    
        def search(s):
            if s in mem:
                return mem[s]

            if len(s) == 0:
                return [""]
            
            res = []       
            for i in range(0, len(s) + 1):
                if s[:i] in wordSet:
                    subRes = search(s[i:])
                    res += [s[:i] + " " + sub if sub != "" else s[:i] + "" + sub for sub in subRes]
                    
            mem[s] = res
            return res
        
        return search(s)
        
x = Solution()
print(x.wordBreak("pineapplepenapple", ["apple", "pen", "applepen", "pine", "pineapple"]))