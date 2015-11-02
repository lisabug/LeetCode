#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'Yuanqin Lu'

class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        T = nums[0]
        maxsub = T
        for num in nums[1:]:
            T += num
            # T is minus
            if num > T:
                T = num
            if T > maxsub:
                maxsub = T

        return maxsub
