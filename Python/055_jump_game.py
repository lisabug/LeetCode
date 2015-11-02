#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'Yuanqin Lu'

class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        l = len(nums)
        if l < 2:
            return True
        i = 0
        while nums[i]:
            max_jump = 0
            next_jump = -1
            for j in xrange(1, nums[i]+1):
                if i+j >= l-1:
                    return True
                if j+nums[i+j] >= max_jump:
                    max_jump = j + nums[i+j]
                    next_jump = j
            i += next_jump
        return False

if __name__ == '__main__':
    s = Solution()
    print s.canJump([1,1,2,2,0,1,1])
