class Solution:
    def thirdMax(self, num):
        num = sorted(list(set(num)))

        if len(num) == 0:
            return -1
        elif len(num) == 1:
            return num[0]
        elif len(num) == 2:
            return max(num[0], num[1])
        else:
            return num[-3]


s = Solution()
# print(s.thirdMax([]))
# print(s.thirdMax([1]))
# print(s.thirdMax([3, 1]))
# print(s.thirdMax([2, 2, 3, 1]))
# print(s.thirdMax([-1, 2, 3]))
# print(s.thirdMax([-1, -2, -3]))
print(s.thirdMax([1, 2, 3, -1, -2, -3]))
