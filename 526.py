class Solution:
    
    def dfs(self, p, used, N):
        if p >= N:
            self.count += 1
        
        for i, n in enumerate(used):
            if n == 0 and ((p + 1) % (i + 1) == 0 or (i + 1) % (p + 1) == 0):
                # not used
                used[i] = 1
                self.dfs(p + 1, used, N)
                used[i] = 0
            
        
        
    def countArrangement(self, N: int) -> int:
        self.count = 0    
        
        used = [0 for i in range(N)]
        
        self.dfs(0, used, N)
        
        return self.count

print(Solution().countArrangement(2))