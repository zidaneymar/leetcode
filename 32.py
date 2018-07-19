class Solution:
    def longestValidParentheses(self, s: str):
        """
        :type s: str
        :rtype: int
        """
        #dp = [[False for x in len(str)] for y in len(str)]
        mem = {}
        maxLength = 0
        minI = len(s)
        maxJ = 0
        def dp(i, j):
            nonlocal maxLength
            nonlocal minI
            nonlocal maxJ
            if (i, j) in mem:
                return mem[(i, j)]
            res0 = res1 = res2 = res3 = False
            if i >= j:
                return False
            if i < 0 or i >= len(s) or j < 0 or j >= len(s):
                return False
            if i == j - 1:
                res0 = (s[i] == '(' and s[j] == ')')
            res1 = (s[i] == '(' and s[j] == ')' and dp(i+1, j-1))
            if i + 1 < len(s) and i >= 0:
                res2 = (s[i] == '(' and s[i+1] == ')' and dp(i+2, j))
            if j - 1 >= 0 and j < len(s):
                res3 = (s[j] == ')' and s[j-1] == '(' and dp(i, j-2))
            res = res1 or res2 or res3 or res0
            mem[(i, j)] = res
            if res:
                maxLength = max(maxLength, abs(j + 1 - i))
                maxJ = max(j, maxJ)
                minI = min(i, minI)
            return res
        for i in range(0, len(s)):
            for j in range(0, len(s)):
                dp(i, i + j)

        print(s)
        for i in range(0, minI):
            print("X", end='')
        print(s[i:j+1], end='')
        for j in range(maxJ + 1, len(s)):
            print("X", end='')

        return maxLength

x = Solution()

print(x.longestValidParentheses(")(((((()())()()))()(()))("))
        