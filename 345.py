class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = list(s)
        v = "aeiou"
        start = 0
        end = len(s) - 1
        while start < end:
            while s[start] not in v:
                start += 1
            while s[end] not in v:
                end -= 1
            if start >= end:
                break
            
            buf = s[start]
            s[start] = s[end]
            s[end] = buf
            start += 1
            end -= 1
        
        return str(s)

print(Solution().reverseVowels("leetcode"))