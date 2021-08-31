class Solution:
    def isPalindrome(self, s):

        s = ''.join(e for e in s if e.isalnum())
        s = s.lower()
        if s == s[::-1]:
            return True
        else:
            return False


s = Solution()
string = "A man, a plan, a canal: Panama"
print(s.isPalindrome(string))
