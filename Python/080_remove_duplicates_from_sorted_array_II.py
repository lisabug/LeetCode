#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'Yuanqin Lu'

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        for i, num in enumerate(nums):
            if count < 2 or nums[i] != nums[count-1] or nums[i] != nums[count-2]:
                nums[count] = num
                count += 1
        return count
