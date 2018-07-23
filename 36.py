class Solution:
    def isValidSudoku(self, board: list):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        empty = "."
        
        # row validation
        for i in range(0, len(board)):
            flag_r = [None] * 10
            flag_c = [None] * 10
            for j in range(0, len(board[i])):
                cur = board[i][j]
                if cur != empty:
                    if flag_r[int(cur) - 1] != None:
                        return False
                    flag_r[int(cur) - 1] = True
                
                cur = board[j][i]
                if cur != empty:
                    if flag_c[int(cur) - 1] != None:
                        return False
                    flag_c[int(cur) - 1] = True



        for i in range(0, int(len(board) / 3)):
            for j in range(0, int(len(board) / 3)):
                flag = [None] * 10
                for k in range(0, 3):
                    for l in range(0, 3):
                        cur = board[i * 3 + k][j * 3 + l]
                        if cur != ".":
                            if flag[int(cur) - 1] != None:
                                return False
                            flag[int(cur) - 1] = True
        return True

x = Solution()

print(x.isValidSudoku([
  ["5","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]))