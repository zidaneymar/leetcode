class Solution:

    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        a = [[0 for i in range(n)] for j in range(n)]
        direction = 'r'
        value = 1
        i = 0
        j = 0
        while value <= n * n:
            if direction == 'r':
                a[i][j] = value
                value += 1
                if (j < n - 1 and a[i][j+1]) or j == n - 1:
                    direction = 'd'
                    i += 1
                else:
                    j += 1
            elif direction == 'd':           
                a[i][j] = value
                value += 1
                if (i < n - 1 and a[i+1][j]) or i == n - 1:
                    direction = 'l'
                    j -= 1
                else:
                    i += 1

            elif direction == 'l':
                a[i][j] = value
                value += 1
                if (j >= 1 and a[i][j-1]) or j == 0:
                    direction = 'u'
                    i -= 1
                else:
                    j -= 1

            elif direction == 'u':
                a[i][j] = value
                value += 1
                if (i >= 1 and a[i-1][j]) or i == 0:
                    direction = 'r'
                    j += 1
                else:
                    i -= 1
        return a

x = Solution()
print(x.generateMatrix(3))


