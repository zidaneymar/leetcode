class Solution:
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        path_list = path.split("/")
        
        path_stack = []

        for path in path_list:
            if path != "/" and path != "." and path != ".." and path != "":
                path_stack.append(path)
            if path == "..":
                if len(path_stack) > 0:
                    path_stack.pop()
        
        res = "/" + "/".join(path_stack)

        return res

x = Solution()

print(x.simplifyPath("/a/./b/../../c/"))
print(x.simplifyPath("/../"))
print(x.simplifyPath("/home//foo/"))