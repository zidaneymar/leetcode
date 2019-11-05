class Solution:
    
    def findPath(self, board, word, i, j, visited):
        if (i, j) in visited:
            return False
        if len(word) == 0:
            return True
        
        visited.add((i, j))
        
        c = word[0]
        res1 = res2 = res3 = res4 = False
        if i - 1 >= 0 and board[i - 1][j] == c:
            res1 = self.findPath(board, word[1:], i - 1, j, visited)
        if i + 1 < len(board) and board[i + 1][j] == c:
            res2 = self.findPath(board, word[1:], i + 1, j, visited)
        if j - 1 >= 0 and board[i][j - 1] == c:
            res3 = self.findPath(board, word[1:], i, j - 1, visited)
        if j + 1 < len(board[0]) and board[i][j + 1] == c:
            res4 = self.findPath(board, word[1:], i, j + 1, visited)
        
        visited.remove((i, j))
        
        return res1 or res2 or res3 or res4
        
    
    def findWords(self, board, words):
        
        index = {}
        
        for i, row in enumerate(board):
            for j, c in enumerate(row):
                if c in index:
                    index[c].append((i, j))
                else:
                    index[c] = [(i, j)]
        
        
        res = []
        
        for w in words:
            
            if w[0] in index:
                for loc in index[w[0]]:
                    i, j = loc
                    if self.findPath(board, w[1:], i, j, set()):
                        res.append(w)
                                        
        return res


print(Solution().findWords([
  ['o','a','a','n'],
  ['e','t','a','e'],
  ['i','h','k','r'],
  ['i','f','l','v']
], ["oath","pea","eat","rain"]
))