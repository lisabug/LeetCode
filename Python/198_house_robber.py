#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'Yuanqin Lu'

class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        l = len(nums)
        if l == 1:
            return nums[0]
        f1, f2 = nums[0], max(nums[0], nums[1])
        for num in nums[2:]:
            f1, f2 = f2, max(num + f1,f2)
        return f2
