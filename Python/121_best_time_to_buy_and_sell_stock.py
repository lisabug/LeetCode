#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'Yuanqin Lu'

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) == 0:
            return 0

        buy = prices[0]
        max_profit = 0
        for price in prices[1:]:
            if price < buy:
                buy = price
            profit = price - buy
            if profit > max_profit:
                max_profit = profit

        return max_profit
