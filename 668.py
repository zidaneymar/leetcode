class Solution:
    def upperBound(self, m, n, target):
        return min(target // (m + 1), n)
    
    def findKthNumber(self, m: int, n: int, k: int) -> int:
        
        
        low = 1
        high = m * n
        
        while low < high:
            num = 0
            mid = low + (high - low) // 2
            for i in range(0, m):
        
                num += self.upperBound(i, n, mid)
            
            if num < k:
                low = mid + 1
            else:
                high = mid
        
        return low


print(Solution().findKthNumber(3, 3, 5))