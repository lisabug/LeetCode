#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'Yuanqin Lu'

class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        upper, below, left, right = 0, n, 0, n
        # initilation
        ret = [[0 for _ in xrange(n)] for _ in xrange(n)]
        num = 1
        while upper < below and left < right:
            # right
            for j in xrange(left, right):
                ret[upper][j] = num
                num += 1
            upper += 1
            # down
            for i in xrange(upper, below):
                ret[i][right-1] = num
                num += 1
            right -= 1
            # left
            for j in xrange(right-1, left-1, -1):
                ret[below-1][j] = num
                num += 1
            below -= 1
            # up
            for i in xrange(below-1, upper-1, -1):
                ret[i][left] = num
                num += 1
            left += 1
        return ret
