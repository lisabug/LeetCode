#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'Yuanqin Lu'

class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        pathSum = [-1 for x in xrange(len(triangle))]
        pathSum[0] = triangle[0][0]
        for row in triangle[1:]:
            lastSum = list(pathSum)
            for j, num in enumerate(row):
                if j == 0:
                    pathSum[j] = lastSum[j] + num
                elif j == len(row)-1:
                    pathSum[j] = lastSum[j-1] + num
                else:
                    pathSum[j] = min(lastSum[j-1], lastSum[j]) + num

        return min(pathSum)
