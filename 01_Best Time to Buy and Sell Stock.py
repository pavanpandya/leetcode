p = input()
bad_chars = ['[', ']', ' ', ',']

for i in bad_chars:
    p = p.replace(i, '')

p = list(map(int, p))


def find_best_stock(p):
    s = []
    for i in range(len(p)):
        for j in range(i, len(p)):
            ans = p[j] - p[i]
            s.append(ans)

    # print(s)
    return max(s)


print(find_best_stock(p), end="")

# # Second Approach
# class Solution:
#     def maxProfit(self, prices):
#         max_profit = 0
#         min_price = float('inf')

#         for current_price in prices:
#             min_price = min(min_price, current_price)
#             # profit = current_price - min_price
#             # max_profit = max(max_profit, profit)
#             max_profit = max(max_profit, current_price - min_price)

#         return max_profit


# s = Solution()
# print(s.maxProfit([5, 4, 1, 7, 8]))
