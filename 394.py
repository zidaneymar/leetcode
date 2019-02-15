class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        def findTheOtherIndex(s):
            count = 0
            for i in range(0, len(s)):
                if s[i] == '[':
                    count += 1
                elif s[i] == ']':
                    count -= 1
                if count == 0:
                    return i
            
        def dfs(s):
            curNum = 0
            i = 0
            res = ""
            while i < len(s):
                if s[i] >= '0' and s[i] <= '9':
                    curNum *= 10
                    curNum += int(s[i])
                elif s[i] == '[':
                    
                    rIndex = findTheOtherIndex(s[i:])
                    res += curNum * dfs(s[i + 1:i + rIndex])
                    i = i + rIndex
                    curNum = 0
                elif s[i].lower() >= 'a' and s[i].lower() <= 'z':
                    res += s[i]
                
                i += 1
            return res
        
        return dfs(s)

print(Solution().decodeString("100[leetcode]"))