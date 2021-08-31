class Solution:
    def plusOne(self, num):

        # num = [1,2,3]
        arr = [str(num) for num in num]
        num = "".join(arr)
        num = int(num)
        num = num + 1
        num = [int(x) for x in str(num)]
        return num


s = Solution()
print(s.plusOne([9, 9, 9]))
