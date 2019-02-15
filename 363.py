
class Solution:
    def maxSumSubmatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        if len(matrix) == 0:
            return 0
        s = [[0 for i in range(0, len(matrix[0]))]
             for j in range(0, len(matrix))]

        res = -float('inf')

        for i in range(0, len(matrix[0])):
            for j in range(0, len(matrix)):
                if i < 1 and j < 1:
                    s[j][i] = matrix[j][i]
                elif j < 1:
                    s[j][i] = s[j][i - 1] + matrix[j][i]
                elif i < 1:
                    s[j][i] = s[j - 1][i] + matrix[j][i]
                else:
                    s[j][i] = s[j - 1][i] + s[j][i - 1] - s[j - 1][i - 1] + matrix[j][i]

                if s[j][i] < target:
                    res = max(res, s[j][i])
                elif s[j][i] == target:
                    return target

        for i in range(0, len(matrix[0]) + 1):
            for j in range(0, len(matrix) + 1):
                for k in range(i, len(matrix[0]) + 1):
                    for l in range(j, len(matrix) + 1):
                        if i == j == k == l:
                            continue
                        if l >= 1 and k >= 1:
                            if i >= 1 and j >= 1:
                                curSum = s[l - 1][k - 1] - s[l - 1][i - 1] - s[j - 1][k - 1] + s[j - 1][i - 1]
                            elif i >= 1:
                                curSum = s[l - 1][k - 1] - s[l - 1][i - 1]
                            elif j >= 1:
                                curSum = s[l - 1][k - 1] - s[j - 1][k - 1]
                            else:
                                curSum = s[l - 1][k - 1]
                            if curSum < target:
                                res = max(res, curSum)
                            elif curSum == target:
                                return target
        return res


x = Solution()
print(x.maxSumSubmatrix([[2,2,-1]], 0))
