class Solution:
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = [i.lower() for i in s if (ord(i) >= ord('0') and ord(i) <= ord('9')) or (ord(i) >= ord('a') and ord(i) <= ord('z')) or (ord(i) >= ord('A') and ord(i) <= ord('Z'))]
        
        if len(s) == 0:
            return True
        low = 0
        high = len(s) - 1
        while low < high:
            if s[low] != s[high]:
                return False
            low += 1
            high -= 1
        return True
        
        

x = Solution()
print(x.isPalindrome("A man, a plan, a canal: Panama"))