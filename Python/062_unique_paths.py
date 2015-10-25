#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'Yuanqin Lu'

class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        pathCount = [[ 0 for i in xrange(n)] for i in xrange(m)]
        for i in xrange(m):
            pathCount[i][0] = 1
        for i in xrange(n):
            pathCount[0][i] = 1
        for i in xrange(1,m):
            for j in xrange(1,n):
                pathCount[i][j] = pathCount[i-1][j] + pathCount[i][j-1]

        return pathCount[-1][-1]
