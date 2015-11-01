#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'Yuanqin Lu'

class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = len(nums)
        if l == 1:
            return nums[0]
        positive = [0 for _ in xrange(l+1)]
        negative = list(positive)
        max_product = 0
        for i in xrange(1, l+1):
            if nums[i-1] > 0:
                positive[i] = positive[i-1] * nums[i-1] if positive[i-1] else nums[i-1]
                negative[i] = negative[i-1] * nums[i-1] if negative[i-1] else 0
            elif nums[i-1] < 0:
                positive[i] = negative[i-1] * nums[i-1] if negative[i-1] else 0
                negative[i] = positive[i-1] * nums[i-1] if positive[i-1] else nums[i-1]
            max_product = max(max_product, positive[i])

        return max_product

    def maxProduct1(self, nums):
        ret=small=big=nums[0]
        for n in nums[1:]:
            big, small = max(n, n*big, n*small), min(n, n*big, n*small)
            ret = max(big, ret)
        return ret
