#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'Yuanqin Lu'

class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        if not obstacleGrid or not obstacleGrid[0]:
            return 0

        m = len(obstacleGrid)
        n = len(obstacleGrid[0])

        pathCount = [[0 for i in xrange(n)] for i in xrange(m)]
        for i in xrange(m):
            if obstacleGrid[i][0] == 1:
                break
            else:
                pathCount[i][0] = 1
        for i in xrange(n):
            if obstacleGrid[0][i] == 1:
                break
            else:
                pathCount[0][i] = 1

        for i in xrange(1,m):
            for j in xrange(1,n):
                if obstacleGrid[i][j] == 1:
                    continue
                else:
                    pathCount[i][j] = pathCount[i-1][j] + pathCount[i][j-1]

        return pathCount[-1][-1]
