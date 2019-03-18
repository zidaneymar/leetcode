import heapq

class Solution:

    def getMedian(self, minq, maxq):
        if len(minq) > len(maxq):
            return minq[0]
        elif len(minq) < len(maxq):
            return -maxq[0]
        else:
            return (minq[0] + -maxq[0]) / 2
    
    def add(self, minq, maxq, val):
        if len(minq) == len(maxq) == 0:
            minq.append(val)
            return
        if val > self.getMedian(minq, maxq):
            heapq.heappush(minq, val)
        else:
            heapq.heappush(maxq, -val)
        
        if len(minq) > len(maxq) + 1:
            temp = minq[0]
            heapq.heappop(minq)
            heapq.heappush(maxq, -temp)
        elif len(maxq) > len(minq) + 1:
            temp = maxq[0]
            heapq.heappop(maxq)
            heapq.heappush(minq, temp)
    
    def remove(self, minq, maxq, val, start):
        if start == 0:
            return
        if val in minq:
            minq.remove(val)
            heapq.heapify(minq)
        elif -val in maxq:
            maxq.remove(-val)
            heapq.heapify(maxq)
        
        
    def medianSlidingWindow(self, nums, k: int):
        minq = []
        maxq = []
        res = []
        index = 0
        for start in range(0, len(nums) - k + 1):
            
            self.remove(minq, maxq, nums[start - 1], start)
            
            while len(minq) + len(maxq) < k:
                self.add(minq, maxq, nums[index])
                index += 1
            res.append(self.getMedian(minq, maxq))
            
        return res
            
            
            
print(Solution().medianSlidingWindow([1,3,-1,-3,5,3,6,7], 3))