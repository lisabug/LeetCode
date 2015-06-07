#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @author: Yuanqin Lu

class Solution:
    # @param {integer[]} nums
    # @param {integer} val
    # @return {integer}
    def removeElement(self, nums, val):
        if not nums:
            return 0
        n = 0
        for i in xrange(len(nums)):
            if nums[i] != val:
                nums[n] = nums[i]
                n += 1
        nums = nums[:n]
        return n
