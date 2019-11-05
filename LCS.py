


# get concrete longest common subsequence

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
    
