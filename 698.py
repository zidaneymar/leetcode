

class Solution:
    def dfs(self, nums, k, target, cur, index, visited):
        
        if index >= len(cur):
            return True
        
        for i, n in enumerate(nums):
            if visited[i] == 0:
                if cur[index] + n <= target:
                    cur[index] += n
                    visited[i] = 1
                    res = False
                    if cur[index] == target:
                        res = self.dfs(nums, k, target, cur, index + 1, visited)
                    else:
                        res = self.dfs(nums, k, target, cur, index, visited)
                        
                    if res:
                        return True
                    visited[i] = 0
                    cur[index] -= n
        return False
    def canPartitionKSubsets(self, nums, k: int) -> bool:
        total = sum(nums)
        
        if total % k != 0:
            return False
    
        target = total // k
        
        visited = [0] * len(nums)
        
        cur = [0] * k
        
        return self.dfs(nums, k, target, cur, 0, visited)

print(Solution().canPartitionKSubsets([4, 3, 2, 3, 5, 2, 1], 4))