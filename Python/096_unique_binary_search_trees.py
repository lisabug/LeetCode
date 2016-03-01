#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'Yuanqin Lu'

class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [0 for _ in xrange(n+1)]
        dp[0], dp[1] = 1, 1
        for i in xrange(2, n+1):
            for j in xrange(1, i+1):
                dp[i] += dp[j-1]*dp[i-j]
        return dp[-1]
