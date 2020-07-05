#
# @lc app=leetcode.cn id=55 lang=python
#
# [55] 跳跃游戏
#

# @lc code=start
class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if nums == [0]: return True
        maxDist = 0
        end_index = len(nums)-1
        for i, jump in enumerate(nums):
            if maxDist >= i and i+jump > maxDist:
                maxDist = i+jump
                if maxDist >= end_index:
                    return True
        
        return False
# @lc code=end

