#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @author: Yuanqin Lu

class Solution:
    # @param {integer} dividend
    # @param {integer} divisor
    # @return {integer}
    def divide(self, dividend, divisor):
        MAX_INT = 0xFFFFFFFF/2
        MIN_INT = ~0xFFFFFFFF/2

        a = abs(dividend)
        b = abs(divisor)

        if (dividend < 0) ^ (divisor < 0):
            sign = -1
        else:
            sign = 1

        if b == 0 or (dividend == MIN_INT and divisor == -1):
            print 1
            return MAX_INT
        elif b == 1:
            print 2
            return sign*a

        result = 0
        while a >= b:
            i = 0
            while a >= (b << i):
                a -= b<<i
                result += 1<<i
                i += 1

        return result*sign

if __name__ == '__main__':
    s = Solution()
    print s.divide(-2147483648, -1)
