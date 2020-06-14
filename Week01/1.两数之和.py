#
# @lc app=leetcode.cn id=1 lang=python
#
# [1] 两数之和
#

# @lc code=start
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        n = len(nums)
        for x in range(n):
            for y in range(x+1 , n):
                if nums[x] + nums[y] == target:
                    return x , y
                    break
                else:
                    continue
        
# @lc code=end

