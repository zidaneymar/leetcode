class Solution:
    def groupAnagrams(self, strs: list):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """

        def generate_tuple_key(_str):
            a = [0] * 26
            for char in _str:
                a[ord(char) - ord('a')] += 1 
            return tuple(a)
        stored = dict()
        for _str in strs:
            key = generate_tuple_key(_str)
            if key in stored.keys():
                stored[key].append(_str)
            else:
                stored[key] = [_str]
        result = []
        for key in stored.keys():
            result.append(stored[key])
        return result

x = Solution()
print(x.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
            
        