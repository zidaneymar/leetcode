class Solution:
    def searchMatrix(self, matrix: list, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        
        # row = len(matrix)
        # column = len(matrix[0])

        # def search(matrix: list, target, low_i, low_j)


        line = []
        for row in matrix:
            line += row
        
        if len(line) <= 0:
            return False
        low = 0
        high = len(line) - 1
        while low <= high:
            mid = int((low + high) / 2)
            if line[mid] == target:
                return True
            elif line[mid] > target:
                high = mid - 1
            elif line[mid] < target:
                low = mid + 1
        return False


x = Solution()
print(x.searchMatrix([
  [1]], 13))