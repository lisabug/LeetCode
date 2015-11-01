#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'Yuanqin Lu'

class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix or not matrix[0]:
            return 0
        m = len(matrix)
        n = len(matrix[0])
        L = [0] * n
        H = [0] * n
        R = [n] * n
        ret = 0
        for i in xrange(m):
            left = 0
            right = n
            # update height and left
            for j in xrange(n):
                if matrix[i][j] == '1':
                    H[j] += 1
                    L[j] = max(L[j], left)
                else:
                    left = j + 1
                    H[j] = 0
                    L[j] = 0
                    R[j] = n
            # update right
            for j in range(n)[::-1]:
                if matrix[i][j] == '1':
                    R[j] = min(right, R[j])
                    ret = max(ret, (min(R[j]-L[j], H[j]))**2)
                else:
                    right = j

        return ret


