class Solution:
    def setZeroes(self, matrix: list):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        rows = len(matrix)
        columns = len(matrix[0])
        col1 = None

        for i in range(0, rows):
            if matrix[i][0] == 0:
                col1 = 0
                break
        
        for i in range(0, rows):
            for j in range(0, columns):
                if matrix[i][j] == 0:
                    if j != 0:
                        matrix[0][j] = 0
                    matrix[i][0] = 0
        
        for i in reversed(range(0, rows)):
            for j in reversed(range(1, columns)):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
        
        for i in range(0, rows):
            if col1 == 0:
                matrix[i][0] = 0

        #return matrix


x = Solution()

print(x.setZeroes([
  [1,1,1],
  [1,0,1],
  [1,1,1]
]))