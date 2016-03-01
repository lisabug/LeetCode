#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'Yuanqin Lu'

class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def helper(res, tmpList, nums, begin):
            res.append(tmpList)
            for i in xrange(begin, len(nums)):
                if i == begin or (nums[i] != nums[i-1]):
                    helper(res, tmpList+[nums[i]], nums, i+1)
        if not nums:
            return []
        nums.sort()
        res = []
        helper(res, [], nums, 0)
        return res
