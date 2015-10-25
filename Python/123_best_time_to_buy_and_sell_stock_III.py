#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'Yuanqin Lu'

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        n = len(prices)
        if n < 2:
            return 0
        f = [0 for i in xrange(n)]
        g = list(f)

        valley = prices[0]
        i = 1
        while i < n:
            valley = min(valley, prices[i])
            f[i] = max(f[i-1], prices[i] - valley)
            i += 1

        i = n - 2
        peak = prices[-1]
        while i >= 0:
            peak = max(peak, prices[i])
            g[i] = max(g[i+1], peak - prices[i])
            i -= 1

        max_profit = 0
        for ff, gg in zip(f,g):
            max_profit = max(max_profit, ff+gg)

        return max_profit
