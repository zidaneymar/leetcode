import collections
class Solution:
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """

        
        visited = set()
        if len(board) == 0 or len(board[0]) == 0:
            return
        width = len(board[0])
        height = len(board)

                
        def bfs(board, i, j):
            width = len(board[0])
            height = len(board)
            queue = collections.deque()
            if (i, j) not in visited and board[j][i] == 'O':
                queue.append((i, j))
                visited.add((i, j))
            while len(queue) > 0:
                top = queue.popleft()
                x = top[0]
                y = top[1]
                
                if x - 1 >= 0 and board[y][x - 1] == 'O' and (x - 1, y) not in visited:
                    queue.append((x - 1, y))
                    visited.add((x - 1, y))
                if y - 1 >= 0 and board[y - 1][x] == 'O' and (x, y - 1) not in visited:
                    queue.append((x, y - 1))
                    visited.add((x, y - 1))
                if x + 1 < width and board[y][x + 1] == 'O' and (x + 1, y) not in visited:
                    queue.append((x + 1, y))
                    visited.add((x + 1, y))
                if y + 1 < height and board[y + 1][x] == 'O' and (x, y + 1) not in visited:
                    queue.append((x, y + 1))
                    visited.add((x, y + 1))
                    
        for i in range(0, width):
            if board[0][i] == 'O' and (i, 0) not in visited:
                bfs(board, i, 0)
            if board[height - 1][i] == 'O' and (i, height - 1) not in visited:
                bfs(board, i, height - 1)
        
        for j in range(0, height):
            if board[j][0] == 'O' and (0, j) not in visited:
                bfs(board, 0, j)
            if board[j][width - 1] == 'O' and (width - 1, j) not in visited:
                bfs(board, width - 1, j)
        
        for i in range(0, width):
            for j in range(0, height):
                if (i, j) not in visited:
                    board[j][i] = 'X'
        
        
x = Solution()
board = [["X","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O"],["O","X","O","O","O","O","X","O","O","O","O","O","O","O","O","O","O","O","X","X"],["O","O","O","O","O","O","O","O","X","O","O","O","O","O","O","O","O","O","O","X"],["O","O","X","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","X","O"],["O","O","O","O","O","X","O","O","O","O","X","O","O","O","O","O","X","O","O","X"],["X","O","O","O","X","O","O","O","O","O","X","O","X","O","X","O","X","O","X","O"],["O","O","O","O","X","O","O","X","O","O","O","O","O","X","O","O","X","O","O","O"],["X","O","O","O","X","X","X","O","X","O","O","O","O","X","X","O","X","O","O","O"],["O","O","O","O","O","X","X","X","X","O","O","O","O","X","O","O","X","O","O","O"],["X","O","O","O","O","X","O","O","O","O","O","O","X","X","O","O","X","O","O","X"],["O","O","O","O","O","O","O","O","O","O","X","O","O","X","O","O","O","X","O","X"],["O","O","O","O","X","O","X","O","O","X","X","O","O","O","O","O","X","O","O","O"],["X","X","O","O","O","O","O","X","O","O","O","O","O","O","O","O","O","O","O","O"],["O","X","O","X","O","O","O","X","O","X","O","O","O","X","O","X","O","X","O","O"],["O","O","X","O","O","O","O","O","O","O","X","O","O","O","O","O","X","O","X","O"],["X","X","O","O","O","O","O","O","O","O","X","O","X","X","O","O","O","X","O","O"],["O","O","X","O","O","O","O","O","O","O","X","O","O","X","O","X","O","X","O","O"],["O","O","O","X","O","O","O","O","O","X","X","X","O","O","X","O","O","O","X","O"],["O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O"],["X","O","O","O","O","X","O","O","O","X","X","O","O","X","O","X","O","X","O","O"]]
print(x.solve(board))