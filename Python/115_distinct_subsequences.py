#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'Yuanqin Lu'

class Solution(object):
    def numDistinct(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        l1, l2 = len(s)+1, len(t)+1
        state = [[1] * l2 for _ in xrange(l1)]
        for j in xrange(1, l2):
            state[0][j] = 0
        for i in xrange(1,l1):
            for j in xrange(1,l2):
                state[i][j] = state[i-1][j] + state[i-1][j-1]*(s[i-1] == t[j-1])

        return state[-1][-1]
