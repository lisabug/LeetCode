#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'Yuanqin Lu'

class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        nums = map(str, range(1, n+1))
        k -= 1
        factor = 1
        for i in xrange(1,n):
            factor *= i
        ret = list()
        k = k % (factor*n)
        for i in reversed(xrange(n)):
            ret.append(nums[k/factor])
            nums.remove(nums[k/factor])
            if i != 0:
                k %= factor
                factor /= i

        return "".join(ret)
