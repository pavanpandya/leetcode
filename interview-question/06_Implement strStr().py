class Solution:
    def strStr(self, haystack, needle):
        if len(needle) == 0:
            return 0
        elif needle in haystack:
            return haystack.find(needle)
        else:
            return -1


s = Solution()
haystack = "hello"
needle = "ll"
print(s.strStr(haystack, needle))
