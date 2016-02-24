#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'Yuanqin Lu'

class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def helper(candidates, val, start, res):
            res.append(val)
            for i in xrange(start, len(candidates)):
                helper(candidates, val+[candidates[i]], i+1, res)

        result, tmp = list(), list()
        nums.sort()
        helper(nums, tmp, 0, result)
        return result
