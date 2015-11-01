#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'Yuanqin Lu'

class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def _rob(nums):
            if len(nums) == 1:
                return nums[0]
            f1, f2 = nums[0], max(nums[0], nums[1])
            for num in nums[2:]:
                f1, f2 = f2, max(f2, num+f1)
            return f2
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        return max(_rob(nums[:-1]), _rob(nums[1:]))
