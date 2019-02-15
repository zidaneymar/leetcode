class Solution:
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        res = []
        
        
        def isPalindorme(s):
            if len(s) == 0:
                return False
            if len(s) == 1:
                return True
            low = 0
            high = len(s) - 1
            while low < high:
                if s[low] != s[high]:
                    return False
                low += 1
                high -= 1
            return True
        

        def dfs(s, start, end, cur_res):
            if start == end == len(s):
                res.append(cur_res)
                return
            
            if end > len(s) or start > len(s):
                return 
            if isPalindorme(s[start:end]):
                dfs(s, end, end, cur_res + [s[start:end]])
            dfs(s, start, end + 1, cur_res)
            
        dfs(s, 0, 0, [])
        return res
        
x = Solution()
print(x.partition('aab'))