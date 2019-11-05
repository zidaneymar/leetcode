import heapq
class Solution:
    def swimInWater(self, grid) -> int:
        R, C = len(grid) - 1, len(grid[0]) - 1
        dirs = ((0, 1), (0, -1), (1, 0), (-1, 0))
        max_price = grid[0][0]
        q = [(max_price, 0, 0)]
        visited = [[False]*(C+1) for _ in range(R+1)]
        visited[0][0] = True
        while q:
            p, r, c = heapq.heappop(q)
            max_price = max(max_price, p)
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if 0 <= nr <= R and 0 <= nc <= C and not visited[nr][nc]:
                    if nr == R and nc == C:
                        return max(max_price, grid[nr][nc])
                    heapq.heappush(q, (grid[nr][nc], nr, nc))
                    visited[nr][nc] = True
print(Solution().swimInWater([[0,1,2,3,4],[24,23,22,21,5],[12,13,14,15,16],[11,17,18,19,20],[10,9,8,7,6]]))