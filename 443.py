
class Solution:
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        l = 1
        prev = None
        total = len(chars)
        i = 0
        while i <= total:
            if i == total and l != 1:
                chars[i - 1] = str(l)
                break
            if not prev:
                prev = chars[i]
                i += 1
                continue
            if prev == chars[i]:
                chars[i] = ""
                l += 1
                i += 1
            else:
                if l != 1:
                    chars[i - 1] = str(l)
                l = 1
                prev = chars[i]
                i += 1
            
        
            
        # temp = [i for i in chars if i != ""]
        # chars = temp
        return len(chars)


print(Solution().compress(["a","a","b","b","c","c","c"]))