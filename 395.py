class Solution:
    def isValid(self, buf, k):
        for i in buf:
            if i != 0 and i < k:
                return False
        return True
    
    def longestSubstring(self, s: str, k: int) -> int:
        buf = [0] * 26
        
        begin = end = 0
        d = -float('inf')
        while end < len(s):
            
            buf[ord(s[end]) - ord('a')] += 1
            end += 1
            if self.isValid(buf, k):
                
                if end < len(s):
                    if buf[ord(s[end]) - ord('a')] + 1 < k: # the next is invalid, cur is the longest
                        if end - begin > d:
                            d = end - begin
                        buf[ord(s[begin]) - ord('a')] += 1
                        begin += 1
                        
        
        if d == -float('inf'):
            return 0
        
        return d
        
        
print(Solution().longestSubstring("aaabb", 3))