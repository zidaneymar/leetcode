import copy

class Solution:
    def isValid(self, board):
        return board[0][0] == 1 and board[0][1] == 2 and board[0][2] == 3 and board[1][0] == 4 and board[1][1] == 5 and board[1][2] == 0
    
    def getKey(self, board):
        return tuple([tuple(i) for i in board])
    
    
    def slidingPuzzle(self, board) -> int:
        
        
        q = []
        i0 = None
        j0 = None
        for i, r in enumerate(board):
            for j, c in enumerate(r):
                if c == 0:
                    i0 = i
                    j0 = j
                    
        q.append((board, i0, j0, 0))
        
        visited = set()
        
        
        dir = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        
        while len(q) > 0:
            curBoard, i, j, cost = q[0]
            visited.add(self.getKey(curBoard))
            
            del q[0]
            
            for d in dir:
                i1 = i + d[0]
                j1 = j + d[1]
                if i1 not in range(0, 2) or j1 not in range(0, 3):
                    continue
                newBoard = copy.deepcopy(curBoard)
                newBoard[i1][j1], newBoard[i][j] = newBoard[i][j], newBoard[i1][j1]
                newCost = cost + 1
                if self.getKey(newBoard) in visited:
                    continue
        
                if self.isValid(newBoard):
                    return newCost
                
                q.append((newBoard, i1, j1, newCost))
        
        return -1

print(Solution().slidingPuzzle([[1,2,3],[5,4,0]]))
            
            
            
        