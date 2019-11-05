

class Solution:
    def insert(self, intervals, newInterval):
        result = []
        
        i = 0
        
        while i < len(intervals) and intervals[i][1] < newInterval[0]:
            result.append(intervals[i])
            i += 1
        
        
        left = None
        right = None
        
        while i < len(intervals) and intervals[i][0] <= newInterval[1]:
            left = min(newInterval[0], intervals[i][0]) if left else min(newInterval[0], intervals[i][0], left)
            right = max(newInterval[1], intervals[i][1], right) if right else max(newInterval[1], intervals[i][1], right)
            i += 1
        
        if left and right:
            result.append([left, right])
        
        while i < len(intervals):
            result.append(intervals[i])
            i += 1
            
        return result
        
            
print(Solution().insert([[1,2],[3,5],[6,7],[8,10],[12,16]]
,[4,8]))
        