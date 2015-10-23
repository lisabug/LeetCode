#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'Yuanqin Lu'

class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        def available(queens, row, col):
            for k in xrange(row):
                if queens[k] == col or queens[k]-col == k - row or queens[k] - col == row - k:
                    return False
            return True

        def output(queens):
            tmplist = list()
            for queen in queens:
                tmplist.append('.'*queen + 'Q' + '.'*(n-queen-1))
            return tmplist

        queens = [-1 for i in xrange(n)]
        row = 0
        queens[row] = 0
        ret = []
        while row >= 0:
            if row < n and queens[row] < n and available(queens, row, queens[row]):
                if row == n - 1:
                    ret.append(output(queens))
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

        return ret





if __name__ == '__main__':
    s = Solution()
    print s.solveNQueens(4)
