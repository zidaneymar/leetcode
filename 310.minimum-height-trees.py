#
# @lc app=leetcode id=310 lang=python3
#
# [310] Minimum Height Trees
#
# https://leetcode.com/problems/minimum-height-trees/description/
#
# algorithms
# Medium (29.83%)
# Total Accepted:    60.1K
# Total Submissions: 201.5K
# Testcase Example:  '4\n[[1,0],[1,2],[1,3]]'
#
# For an undirected graph with tree characteristics, we can choose any node as
# the root. The result graph is then a rooted tree. Among all possible rooted
# trees, those with minimum height are called minimum height trees (MHTs).
# Given such a graph, write a function to find all the MHTs and return a list
# of their root labels.
# 
# Format
# The graph contains n nodes which are labeled from 0 to n - 1. You will be
# given the number n and a list of undirected edges (each edge is a pair of
# labels).
# 
# You can assume that no duplicate edges will appear in edges. Since all edges
# are undirected, [0, 1] is the same as [1, 0] and thus will not appear
# together in edges.
# 
# Example 1 :
# 
# 
# Input: n = 4, edges = [[1, 0], [1, 2], [1, 3]]
# 
# ⁠       0
# ⁠       |
# ⁠       1
# ⁠      / \
# ⁠     2   3 
# 
# Output: [1]
# 
# 
# Example 2 :
# 
# 
# Input: n = 6, edges = [[0, 3], [1, 3], [2, 3], [4, 3], [5, 4]]
# 
# ⁠    0  1  2
# ⁠     \ | /
# ⁠       3
# ⁠       |
# ⁠       4
# ⁠       |
# ⁠       5 
# 
# Output: [3, 4]
# 
# Note:
# 
# 
# According to the definition of tree on Wikipedia: “a tree is an undirected
# graph in which any two vertices are connected by exactly one path. In other
# words, any connected graph without simple cycles is a tree.”
# The height of a rooted tree is the number of edges on the longest downward
# path between the root and a leaf.
# 
# 
#
class Solution:
   

    def findMinHeightTrees(self, n: int, edges):
        buffer = {}
        indexing = {}
        if len(edges) == 0:
            return [0]
        for e in edges:
            for p in e:
                if p in buffer:
                    buffer[p] += 1
                else:
                    buffer[p] = 1
            p1 = e[0]
            p2 = e[1]
            if p1 in indexing:
                indexing[p1].append(p2)
            else:
                indexing[p1] = [p2]
            if p2 in indexing:
                indexing[p2].append(p1)
            else:
                indexing[p2] = [p1]

        leaf = [i for i in buffer if buffer[i] == 1]
        
        
        while n > 2:
            n -= len(leaf)
            newLeaves = []
            for i in leaf:
                for j in indexing[i]:
                    indexing[j].remove(i)
                    if len(indexing[j]) == 1:
                        newLeaves.append(j)
            leaf = newLeaves
        return leaf

print(Solution().findMinHeightTrees(6,[[0, 3], [1, 3], [2, 3], [4, 3], [5, 4]]))



