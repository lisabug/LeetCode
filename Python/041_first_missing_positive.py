#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'Yuanqin Lu'

class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 0
        n = len(nums)
        while i < n:
            if nums[i] >= 0 and nums[i] < n and nums[nums[i]] != nums[i]:
                nums[nums[i]], nums[i] = nums[i], nums[nums[i]]
            else:
                i += 1

        k = 1
        while k < n:
            if nums[k] != k:
                break
            else:
                k += 1

        if n == 0 or k < n:
            return k
        return k+1 if nums[0] == n else k
