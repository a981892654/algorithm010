#
# @lc app=leetcode.cn id=56 lang=python
#
# [56] 合并区间
#

# @lc code=start
class Solution(object):
    def merge(self, intervals):
        if(not intervals):
            return []
        n=len(intervals)
        intervals.sort()
        res=[]
        left=intervals[0][0]
        right=intervals[0][1]
        for i in range(1,n):
            if(intervals[i][0]<=right):
                if(intervals[i][1]>right):
                    right=intervals[i][1]
            else:
                res.append([left,right])
                left=intervals[i][0]
                right=intervals[i][1]
        res.append([left,right])
        return res
# @lc code=end

