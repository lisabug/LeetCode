#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'Yuanqin Lu'

class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        m = len(word1)
        n = len(word2)

        f = [[0 for i in xrange(n+1)] for i in xrange(m+1)]
        for i in xrange(m+1):
            f[i][0] = i
        for i in xrange(n+1):
            f[0][i] = i

        for i in xrange(1, m+1):
            for j in xrange(1, n+1):
                if word1[i-1] == word2[j-1]:
                    f[i][j] = f[i-1][j-1]
                else:
                    f[i][j] = min(f[i-1][j], min(f[i][j-1], f[i-1][j-1])) + 1

        return f[-1][-1]

