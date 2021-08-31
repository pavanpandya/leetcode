# s = "leetcode"
# s = "loveleetcode"
s = "aatbby"


def find_unique(s):
    for i in range(len(s)):
        if s.count(s[i]) == 1:
            return s.index(s[i])
    return -1


print(find_unique(s))
# print(s.count('b'))
