#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'Yuanqin Lu'

class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        eps = 0.00001
        if x == 0:
            return x
        val = x
        last = val + 1
        while abs(last-val) > eps:
            last = val
            val = (val + float(x)/val) / 2.0

        return int(val)
