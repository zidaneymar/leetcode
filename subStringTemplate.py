class Solution:
    def minWindow(self, s: str, t: str) -> str:
        buf = [0] * 128
        for u in t:
            buf[ord(u)] += 1

        counter = len(t)
        begin = end = 0
        d = float('inf')
        head = 0
        while end < len(s):
            if buf[ord(s[end])] > 0:
                counter -= 1
            buf[ord(s[end])] -= 1
            end += 1
            
            while counter == 0:
                if end - begin < d:
                    head = begin
                    d = end - head
                if buf[ord(s[begin])] == 0:
                    counter += 1
                buf[ord(s[begin])] += 1
                begin += 1
        if d == float('inf'):
            return ""
        return s[head:head + d]