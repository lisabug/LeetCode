#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'Yuanqin Lu'

class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        ways = [1 for _ in xrange(n+1)]
        if n == 1:
            return 1
        else:
            for i in xrange(2, n+1):
                ways[i] = ways[i-1] + ways[i-2]
            return ways[-1]
