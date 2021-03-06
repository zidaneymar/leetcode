class Solution:
    def maxArea(self, height: list) -> int:
        """
        :type height: List[int]
        :rtype: int
        """
        res = 0
        i = 0
        j = len(height) - 1
        while i < j:
            res = max(res, min(height[i], height[j]) * abs(i - j))
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
        return res
                