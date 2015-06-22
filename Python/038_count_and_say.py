#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'Yuanqin Lu'

class Solution:
    # @param {integer} n
    # @return {string}
    def countAndSay(self, n):
        if n == 0:
            return ''
        elif n == 1:
            return str(1)
        else:
            pre = str(1)
            for x in xrange(2,n+1):
                i = 0
                left = 0
                tmp = ''
                while i < len(pre):
                    if pre[i] != pre[left]:
                        tmp += str(i-left)+str(pre[left])
                        left = i
                    else:
                        i += 1
                tmp += str(i-left)+str(pre[left])
                pre = tmp
            return pre
