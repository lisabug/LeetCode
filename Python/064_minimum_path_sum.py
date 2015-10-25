#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'Yuanqin Lu'

class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid or not grid[0]:
            return 0

        m = len(grid)
        n = len(grid[0])

        minSum = [[0 for i in xrange(n)] for i in xrange(m)]
        minSum[0][0] = grid[0][0]
        for i in xrange(1, m):
            minSum[i][0] = minSum[i-1][0] + grid[i][0]
        for i in xrange(1, n):
            minSum[0][i] = minSum[0][i-1] + grid[0][i]
        for i in xrange(1,m):
            for j in xrange(1,n):
                minSum[i][j] = min(minSum[i-1][j], minSum[i][j-1]) + grid[i][j]

        return minSum[-1][-1]
