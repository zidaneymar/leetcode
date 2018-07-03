class Solution:
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        def cal(cur, add, times) -> int:
            nonlocal dividend
            if add + add + cur < dividend:
                return cal(cur, add + add, times + times)
            else:
                return cal(cur + add, add, times)
        return cal(0, divisor, 1)

x = Solution()
print(x.divide(10, 2))