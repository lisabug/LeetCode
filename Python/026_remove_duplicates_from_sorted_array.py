#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @author: Yuanqin Lu

class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def removeDuplicates(self, nums):
        if not nums:
            return 0
        length = len(nums)
        if length == 1:
            return 1
        tmp = nums[0]
        n = 1
        for i in xrange(1, length):
            if nums[i] != tmp:
                nums[n] = nums[i]
                tmp = nums[n]
                n += 1
        nums = nums[:n]
        return n
