class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        
        i = 0
        tag = -1
        
        if len(needle) == 0:
            return 0
        
        if len(needle) > len(haystack):
            return -1
        
        
        for j, n in enumerate(haystack):
            if n == needle[i]:
                if tag == -1:
                    tag = j
                i += 1
            else:
                tag = -1
                i = 0
            if i == len(needle):
                return tag
        return -1
        
print(Solution().strStr("mississippi",
"issip"))