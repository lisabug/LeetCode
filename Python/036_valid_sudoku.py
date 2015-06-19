#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'Yuanqin Lu'

class Solution:
    # @param {character[][]} board
    # @return {boolean}
    def isValidSudoku(self, board):
        row = [{} for x in xrange(9)]
        col = [{} for x in xrange(9)]
        blk = [{} for x in xrange(9)]
        for i in xrange(9):
            for j in xrange(9):
                if board[i][j] == '.': continue
                # row
                if board[i][j] in row[i]: return False
                else: row[i][board[i][j]] = 1
                # col
                if board[i][j] in col[j]: return False
                else: col[j][board[i][j]] = 1
                # block
                if board[i][j] in blk[(i/3)*3+j/3]: return False
                else: blk[i/3*3+j/3][board[i][j]] = 1

        return True

if __name__ == '__main__':
    s = Solution()
    board = [".........","4........","......6..","...38....",".5...6..1","8......6.",".........","..7.9....","...6....."]
    print s.isValidSudoku(board)
