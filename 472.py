
class TrieNode:
    def __init__(self, ch):
        self.subs = [None] * 26
        self.isEnd = False
        self.ch = ch
    def addWord(self, word):
        nodePoint = self
        for i, ch in enumerate(word):
            if nodePoint.subs[ord(ch) - ord('a')] == None:
                nodePoint.subs[ord(ch) - ord('a')] = TrieNode(ch)
            
            if i == len(word) - 1:
                nodePoint.subs[ord(ch) - ord('a')].isEnd = True
            
            nodePoint = nodePoint.subs[ord(ch) - ord('a')]
    def hasWord(self, word):
        nodeP = self
        for i, ch in enumerate(word):
            if nodeP.subs[ord(ch) - ord('a')] != None:
                nodeP = nodeP.subs[ord(ch) - ord('a')]
            else:
                return False
        return nodeP.isEnd
class Solution:
    def findAllConcatenatedWordsInADict(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        root = TrieNode(None)
        for word in words:
            root.addWord(word)

        def dfs(word, count):
            # if the current word could be formed by two subs word
            
            cur = root
            if len(word) == 0:
                return count > 1
            for i, ch in enumerate(word):
                if cur.subs[ord(ch) - ord('a')] == None:
                    return False
                if cur.subs[ord(ch) - ord('a')].isEnd:
                    if dfs(word[i + 1:], count + 1):
                        return True
                cur = cur.subs[ord(ch) - ord('a')]
            return False
        res = []
        for word in words:
            if dfs(word, 0):
                res.append(word)
        return res
print(Solution().findAllConcatenatedWordsInADict(["cat","cats","catsdogcats","dog","dogcatsdog","hippopotamuses","rat","ratcatdogcat"]))