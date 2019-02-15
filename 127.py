import collections


class Solution:
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        def allPossibles(word):
            res = set()
            for j in range(0, len(word)):
                ch = word[j]
                w = [chr(i)
                     for i in range(ord('a'), ord('z') + 1) if chr(i) != ch]
                s = [word[:j] + x + word[j + 1:] for x in w]
                res = res.union(set(s))
            return res

        if endWord not in wordList:
            return 0

        s_queue = collections.deque()
        s_queue.append((beginWord, 1))

        e_queue = collections.deque()
        e_queue.append((endWord, 1))

        s_visited = {}
        e_visited = {}

        s_visited[beginWord] = 1
        e_visited[endWord] = 1

        poss = {}

        for w in wordList + [beginWord]:
            poss[w] = allPossibles(w)

        step = None
        s_radius = None # the radius which w in s meet e_visited
        e_radius = None # the radius which w in e meet s_visited


        while len(s_queue) and len(e_queue):
            s_top = s_queue.popleft()
            s_word = s_top[0]
            s_step = s_top[1]
            e_top = e_queue.popleft()
            e_word = e_top[0]
            e_step = e_top[1]


            if s_radius and s_step > s_radius :
                return step
            if e_radius and e_step > e_radius: # current step is larger than the last meet
                return step
            for w in wordList:
                if w in poss[s_word] and w not in s_visited:
                    if w in e_visited:
                        s_radius = s_step
                        if step:
                            step = min(step, e_visited[w] + s_step)
                        else:
                            step = e_visited[w] + s_step
                    s_queue.append((w, s_step + 1))
                    s_visited[w] = s_step + 1
                if w in poss[e_word] and w not in e_visited:
                    if w in s_visited:
                        e_radius = e_step
                        if step:
                            step = min(s_visited[w] + e_step, step)
                        else:
                            step = s_visited[w] + e_step
                    e_queue.append((w, e_step + 1))
                    e_visited[w] = e_step + 1
        if step:
            return step
        else:
            return 0
x = Solution()

print(x.ladderLength("hit",
"cog",
["hot","dot","dog","lot","log","cog"]))