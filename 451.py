class Solution:
    def frequencySort(self, s: str) -> str:
        
        buf = {}
        for u in s:
            if u not in buf:
                buf[u] = 1
            else:
                buf[u] += 1
        
        most = -1
        for k in buf:
            v = buf[k]
            most = max(most, v)
        
        buck = [None] * most
        
        for k in buf:
            v = buf[k]
            if buck[v - 1] == None:
                buck[v - 1] = [k]
            else:
                buck[v - 1].append(k)
                
        buck = buck[::-1]
        
        res = ''
        for i in range(0, len(buck)):
            unit = buck[i]
            if unit != None:
                for u in unit:
                    res += u * (len(buck) - i)
        return res
print(Solution().frequencySort("tree"))