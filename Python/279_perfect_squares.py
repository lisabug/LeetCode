#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'Yuanqin Lu'

class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        factors = list()
        i = 1
        while i*i <= n:
            factors.append(i*i)
            i += 1
        count = 0
        checker = set([n])
        while 0 not in checker:
            count += 1
            tmp = set()
            for x in checker:
                for y in factors:
                    if x < y:
                        break
                    tmp.add(x-y)
            checker = tmp
        return count


if __name__ == '__main__':
    s = Solution()
    print s.numSquares(12)
