class Solution:
    def lowerBound(self, nums, target):
        
        low = 0
        high = len(nums) - 1
        
        while low < high:
            mid = low + (high - low) // 2
            if nums[mid] < target:
                low = mid + 1
            else:
                high = mid
        
        return low
        
    
    def dfs(self, s, i, j, chars, mem):
       
        if i >= j:
            return 0

        if (i, j) in mem:
            return mem[(i, j)]
        
        res = 0
        for k in range(26):
            newStart = self.lowerBound(chars[k], i)
            newEnd = self.lowerBound(chars[k], j) - 1

            if newStart >= len(chars[k]) or newStart >= j:
                continue

            res += 1

            if newStart != newEnd:
                res += 1

            res += self.dfs(s, newStart + 1, newEnd, chars, mem)

        mem[(i, j)] = res % (10 ** 9 + 7)
        
        return res
    
    def countPalindromicSubsequences(self, S: str) -> int:
        
        
        chars = [[] for _ in range(26)]
        
        for i, ch in enumerate(S):
            chars[ord(ch) - ord('a')].append(i)
        
        
        return self.dfs(S, 0, len(S), chars, {})

print(Solution().countPalindromicSubsequences("bccb"))