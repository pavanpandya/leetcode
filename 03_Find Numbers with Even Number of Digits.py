class Solution:
    def find_num_even(self, n):
        l = []
        for i in range(len(n)):
            r = [int(x) for x in str(n[i])]
            if len(r) % 2 == 0:
                l.append(n[i])
        return len(l)


s = Solution()
# num = int(input())
# bad_chars = ['[', ']', ' ', ',']

# for i in bad_chars:
#     num = num.replace(i, '')

# num = list(map(int, num))
# print(s.find_num_even(num))
print(s.find_num_even([12, 345, 2, 6, 7896]))


# Second Approach
# class Solution:
#     def findNumbers(self, n: List[int]) -> int:
#         l = []
#         for i in range(len(n)):
#             r = [int(x) for x in str(n[i])]
#             if len(r) % 2 == 0:
#                 l.append(n[i])
#         return len(l)
