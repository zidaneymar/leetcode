class Solution:
    def findDiagonalOrder(self, matrix):
        

        buf = [None] * (len(matrix) + len(matrix[0]) - 1)
        
        for rindex, row in enumerate(matrix):
            for cindex, item in enumerate(row):
                if buf[rindex + cindex] == None:
                    buf[rindex + cindex] = []
                buf[rindex + cindex].append(item)
        
        reverse = True
        
        res = []
        for b in buf:
            if reverse:
                res += b[::-1]
                reverse = False
            else:
                res += b
                reverse = True
        return res

print(Solution().findDiagonalOrder([
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]))