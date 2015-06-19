#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'Yuanqin Lu'

class Solution:
    # @param {character[][]} board
    # @return {void} Do not return anything, modify board in-place instead.
    def solveSudoku(self, board):
        self.solver(board)

    def solver(self, board):
        for i in xrange(9):
            for j in xrange(9):
                if board[i][j] == '.':
                    for k in xrange(1,10):
                        if self.isValid(board, i,j,str(k)):
                            board[i][j] = str(k)
                            if self.solver(board):
                                return True
                            else:
                                board[i][j] = '.'
                    return False
        return True

    def isValid(self, board, i, j, c):
        # check row
        for k in xrange(9):
            if c == board[i][k]: return False
        # check column
        for k in xrange(9):
            if c == board[k][j]: return False
        # check block
        for m in xrange(3):
            for n in xrange(3):
                if c == board[m+i/3*3][n+j/3*3]: return False

        return True
