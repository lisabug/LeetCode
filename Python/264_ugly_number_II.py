#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'Yuanqin Lu'

class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        ugly = [0]*n
        i2 = i3 = i5 = -1
        x = v2 = v3 = v5 = 1
        for i in xrange(n):
            x = min(v2,v3,v5)
            ugly[i] = x
            if x == v2:
                i2 += 1
                v2 = ugly[i2]*2
            if x == v3:
                i3 += 1
                v3 = ugly[i3]*3
            if x == v5:
                i5 += 1
                v5 = ugly[i5]*5
        return ugly[-1]
