#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'Yuanqin Lu'

class Solution(object):
    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
        l = len(prices)
        if l < 2:
            return 0
        if k >= l/2:
            max_profit = 0
            for i in xrange(1, l):
                if prices[i-1] < prices[i]:
                    max_profit += prices[i] - prices[i-1]
            return max_profit

        dp = [[0]*l for _ in xrange(k+1)]
        for i in xrange(1, k+1):
            local_max = dp[i-1][0] - prices[0]
            for j in xrange(1, l):
                dp[i][j] = max(dp[i][j-1], local_max + prices[j])
                local_max = max(local_max, dp[i-1][j] - prices[j])
        return dp[-1][-1]

if __name__ == '__main__':
    s = Solution()
    stocks = [3,2,6,5,0,3]
    k = 2
    print s.maxProfit(k, stocks)
