class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        s = str(x)
        value = s[::-1]
        
        return value == s



s = Solution()

print(s.isPalindrome(121))