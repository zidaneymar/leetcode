class Solution:
    def carPooling(self, trips, capacity: int) -> bool:
        cur = 0
        
        temp = [0] * 1000        
        
        for unit in trips:
            x1 = unit[1]
            x2 = unit[2]
            count = unit[0]
            temp[x1] += count
            temp[x2] -= count
        
        for i in temp:
            cur += i
            if cur > capacity:
                return False
        return True
            
print(Solution().carPooling([[2,1,5],[3,5,7]],
3))