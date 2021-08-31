# class Solution:
#     def maxSubArray(self, nums):
#         if len(nums) == 1:
#             return nums[0]

#         max_sum_val = []

#         for i in range(1, len(nums)+1):
#             max_sum = nums[i-1]
#             for j in range(i, len(nums)+1):
#                 current_sum = sum(nums[i-1:j])
#                 max_sum = max(max_sum, current_sum)
#                 max_sum_val.append(max_sum)

#         return max(max_sum_val)

# Second Approach
class Solution:
    def maxSubArray(self, nums):
        if len(nums) == 1:
            return nums[0]

        max_sum = 0

        for num in nums:
            pass

        return max_sum


s = Solution()
# print(s.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
# print(s.maxSubArray([1]))
# print(s.maxSubArray([5, 4, -1, 7, 8]))
