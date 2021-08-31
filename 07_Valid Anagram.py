class Solution:
    def isAnagram(self, s, t):
        s = list(s)
        t = list(t)
        s.sort()
        t.sort()
        
        if len(s) == len(t):
            for i in range(len(s)):
                if s[i] != t[i]:
                    return False

            return True
        else:
            return False



a = Solution()

s = "anagram"
t = "nagaram"

print(a.isAnagram(s, t))
