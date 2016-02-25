#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'Yuanqin Lu'

class Solution(object):
    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """
        def available(queens, row, col):
            for k in xrange(row):
                if queens[k] == col or queens[k]-col == k - row or queens[k] - col == row - k:
                    return False
            return True
        count = 0

        queens = [-1 for i in xrange(n)]
        row = 0
        queens[row] = 0
        while row >= 0:
            if row < n and queens[row] < n and available(queens, row, queens[row]):
                if row == n - 1:
                    count += 1
                    #backtrack
                    row -= 1
                    queens[row] += 1
                else:
                    row += 1
                    queens[row] = 0
            else:
                if queens[row] >= n - 1:
                    row -= 1
                    queens[row] += 1
                else:
                    queens[row] += 1

        return count
