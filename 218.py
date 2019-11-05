import heapq

class Solution:
    def findAndRemove(self, h, p):
        j = 0
        while j < len(h):
            if h[j][1] == p:
                h[j] = (-h[-1][1][2], h[-1][1])
                h.pop()
                break
            j += 1
        heapq.heapify(h)
        
    def getSkyline(self, buildings):
        if len(buildings) == 0:
            return []
        h = []
        res = []


        lines = []
        for b in buildings:
            lines.append((b[0], b))
            lines.append((b[1], b))
        
        lines.sort()
        
        i = 0
        while i < len(lines):
            p = lines[i]
            rec = p[1]
            
            

            if p[0] == rec[0]:
                heapq.heappush(h, (-rec[2], rec))
            
            while len(h) > 0 and h[0][1][1] <= p[0]:
                heapq.heappop(h)

            # if i + 1 < len(lines) and lines[i+1][0] == lines[i][0]:
            #     i += 1
            #     continue

            if len(res) == 0 or (len(h) > 0 and res[-1][1] != h[0][1][2]):
                
                res.append((p[0],h[0][1][2]))
            elif len(h) == 0:
                res.append((p[0], 0))
            i += 1
        return res
                
                
                
        
print(Solution().getSkyline([[2,9,10],[3,7,15],[5,12,12],[15,20,10],[19,24,8]]))