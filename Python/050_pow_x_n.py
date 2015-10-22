#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'Yuanqin Lu'

class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        def _pow(x, n):
            if n == 0:
                return 1
            elif n == 1:
                return x
            elif n == -1:
                return 1.0/x
            else:
                tmp = _pow(x, n/2)
                if n% 2 == 0:
                    return tmp*tmp
                else:
                    return tmp*tmp*x

        return _pow(x,n)
