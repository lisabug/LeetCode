#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'Yuanqin Lu'

class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        def helper(board, notUsed, i, j, word, start):
            if start >= len(word):
                return True
            if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]):
                return False
            if notUsed[i][j] and board[i][j] == word[start]:
                notUsed[i][j] = 0
                if helper(board, notUsed, i+1, j, word, start+1) or helper(board, notUsed, i-1, j, word, start+1) \
                    or helper(board, notUsed, i, j+1, word, start+1) or helper(board, notUsed, i, j-1, word, start+1):
                        return True
                else:
                    notUsed[i][j] = 1
            return False


        if not board or not board[0] or not word:
            return False

        notUsed = [[1 for _ in xrange(len(board[0]))] for _ in xrange(len(board))]
        for i in xrange(len(board)):
            for j in xrange(len(board[0])):
                if board[i][j] == word[0]:
                    notUsed[i][j] = 0
                    if helper(board, notUsed, i-1, j, word, 1) or helper(board, notUsed, i+1, j, word, 1) \
                      or helper(board, notUsed, i, j+1, word, 1) or helper(board, notUsed, i, j-1, word, 1):
                        return True
                    notUsed[i][j] = 1
        return False

if __name__ == '__main__':
    s = Solution()
    board = ["ABCE","SFCS","ADEE"]
    word = "ABCCED"
    print s.exist(board, word)
