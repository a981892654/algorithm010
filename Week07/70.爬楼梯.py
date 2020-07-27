#
# @lc app=leetcode.cn id=70 lang=python
#
# [70] 爬楼梯
#

# @lc code=start
class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        cache = {}
        def climb(n):
            if n in cache:
                return cache[n]
            if n < 3 : return n
            res = climb(n-1) + climb(n-2)
            cache[n] = res
            return res
        return climb(n)
# @lc code=end

