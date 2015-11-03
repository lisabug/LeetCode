#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'Yuanqin Lu'

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        cur = 0
        cnt = 0
        for n in nums:
            if not cnt:
                cur = n
                cnt += 1
            elif cur == n:
                cnt += 1
            else:
                cnt -= 1
        return cur
