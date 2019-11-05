class Solution:
    # return all shortest paths that could from A to the target 
    def dfs(self, curWord, graph, visited, target, mem):
        
        
        
        if curWord == target:
            return [[curWord]]
        

        if curWord in mem:
            return mem[curWord]

        visited.add(curWord)
        
        allSubPaths = []
        for subNode in graph[curWord]:
            if subNode not in visited:
                for path in self.dfs(subNode, graph, visited, target, mem):
                    allSubPaths.append(path)
        
        allSubPaths.sort(key=len)
        
        visited.remove(curWord)

        shortestPaths = [[curWord] + path for path in allSubPaths if len(path) == len(allSubPaths[0])]
        
        mem[curWord] = shortestPaths

        return shortestPaths
            
        
    
    def findLadders(self, beginWord: str, endWord: str, wordList):
        
        wordList.append(beginWord)
        
        wordSet = set(wordList)
        graph = {}
        for word in wordList:
            graph[word] = []
            for i, c in enumerate(word):
                for j in range(0, 26):
                    newWord = word[:i] + chr(ord('a') + j) + word[i + 1:]
                    if newWord in wordSet:
                        graph[word].append(newWord)
        
        return self.dfs(beginWord, graph, set(), endWord, {})

print(Solution().findLadders("qa",
"sq",
["si","go","se","cm","so","ph","mt","db","mb","sb","kr","ln","tm","le","av","sm","ar","ci","ca","br","ti","ba","to","ra","fa","yo","ow","sn","ya","cr","po","fe","ho","ma","re","or","rn","au","ur","rh","sr","tc","lt","lo","as","fr","nb","yb","if","pb","ge","th","pm","rb","sh","co","ga","li","ha","hz","no","bi","di","hi","qa","pi","os","uh","wm","an","me","mo","na","la","st","er","sc","ne","mn","mi","am","ex","pt","io","be","fm","ta","tb","ni","mr","pa","he","lr","sq","ye"])