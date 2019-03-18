#
# @lc app=leetcode id=324 lang=python3
#
# [324] Wiggle Sort II
#
# https://leetcode.com/problems/wiggle-sort-ii/description/
#
# algorithms
# Medium (27.53%)
# Total Accepted:    54.6K
# Total Submissions: 198.4K
# Testcase Example:  '[1,5,1,1,6,4]'
#
# Given an unsorted array nums, reorder it such that nums[0] < nums[1] >
# nums[2] < nums[3]....
# 
# Example 1:
# 
# 
# Input: nums = [1, 5, 1, 1, 6, 4]
# Output: One possible answer is [1, 4, 1, 5, 1, 6].
# 
# Example 2:
# 
# 
# Input: nums = [1, 3, 2, 2, 3, 1]
# Output: One possible answer is [2, 3, 1, 3, 1, 2].
# 
# Note:
# You may assume all input has valid answer.
# 
# Follow Up:
# Can you do it in O(n) time and/or in-place with O(1) extra space?
#
class Solution:
    def wiggleSort(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums.sort()
        before = nums[:len(nums) // 2]
        after = nums[len(nums) // 2:]

        res = []
        while len(before) > 0 and len(after) > 0:
            res.append(before[0])
            res.append(after[0])
            before = before[1:]
            after = after[1:]
        
        res += before + after
        nums = res.copy()

nums = [1,5,1,1,6,4]
Solution().wiggleSort(nums)
print(nums)
