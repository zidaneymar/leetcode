class Solution:
    def lcs(self, str1, str2):
        
        res = [["" for i in range(len(str2) + 1)] for j in range(len(str1) + 1)]
        
        res[0][0] = ""
        
        for i in range(len(str1)):
            for j in range(len(str2)):
                if str1[i] == str2[j]:
                    res[i][j] = res[i - 1][j - 1] + str1[i]
                else:
                    res[i][j] = max(res[i - 1][j], res[i][j - 1], key = len)
        
        return res[-1][-1]
        
    
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        # find the longest common subsequence and contruct the super-sequence from the sub-sequence
        
        res = ""
        temp = self.lcs(str1, str2)
        i = j = 0

        for c in temp:
            while c != str1[i]:
                res += str1[i]
                i += 1
            while c != str2[j]:
                res += str2[j]
                j += 1
            res += c
        return res

print(Solution().shortestCommonSupersequence("aaac", "babc"))