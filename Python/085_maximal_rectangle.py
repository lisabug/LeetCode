#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'Yuanqin Lu'

class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if len(matrix) == 0:
            return 0

        n = len(matrix)
        m = len(matrix[0])

        L = [0 for i in xrange(m)]
        H = [0 for i in xrange(m)]
        R = [m for i in xrange(m)]
        ret = 0

        for row in matrix:
            left = 0
            right = m
            # calculate L(i, j) from left to right
            for j, col in enumerate(row):
                if col == '1':
                    H[j] += 1
                    L[j] = max(L[j], left)
                else:
                    left = j + 1
                    H[j] = 0
                    L[j] = 0
                    R[j] = m
            # calculate R(i, j) from right to left
            j = m - 1
            while j >= 0:
                if row[j] == '1':
                    R[j] = min(right, R[j])
                    ret = max(ret, (R[j] - L[j])*H[j])
                else:
                    right = j
                j -= 1

        return ret


if __name__ == '__main__':
    s = Solution()
    print s.maximalRectangle(['1'])
