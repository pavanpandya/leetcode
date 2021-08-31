# class Solution:
#     def sortColors(self, num):
#         """
#         Do not return anything, modify num in-place instead.
#         """
#         for i in range(len(num)):
#             for j in range(len(num)):
#                 if num[i] < num[j]:
#                     num[i], num[j] = num[j], num[i]

#         return num


# s = Solution()
# num = [2, 0, 2, 1, 1, 0]
# print(s.sortColors(num))


# Second Approach

# def sortnumays(num):

#     length = len(num)
#     j = 0

#     while j < length - 1:
#         if (num[j] > num[j + 1]):
#             num[j], num[j+1] = num[j+1], num[j]
#             j = -1
#         j += 1

#     return num

# Third Approach

num = [2, 0, 2, 1, 1, 0]
p0 = 0
p2 = len(num) - 1
i = 0
while i <= p2:
    if num[i] == 0:
        num[p0], num[i] = num[i], num[p0]
        p0 += 1
        i += 1
    elif num[i] == 2:
        num[i], num[p2] = num[p2], num[i]
        p2 -= 1
    else:
        i += 1

print(num)
