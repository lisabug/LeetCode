#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'Yuanqin Lu'

class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        for i in xrange(n/2):
            k = n-1-i
            for j in xrange(i, k):
                l = n-1-j
                tmp = matrix[i][j]
                matrix[i][j] = matrix[l][i]
                matrix[l][i] = matrix[k][l]
                matrix[k][l] = matrix[j][k]
                matrix[j][k] = tmp


