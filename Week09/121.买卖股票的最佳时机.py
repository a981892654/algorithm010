#
# @lc app=leetcode.cn id=121 lang=python
#
# [121] 买卖股票的最佳时机
#

# @lc code=start
class Solution(object):
    def maxProfit(self, prices):
        if not prices:
            return 0
        min_price = prices[0]
        a = 0
        for i in range(1, len(prices)):
            min_price = prices[i] if min_price > prices[i] else min_price
            a = max(a, prices[i] - min_price)
        return a
# @lc code=end

