#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'Yuanqin Lu'

class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        if not a:
            return b
        if not b:
            return a
        a = map(int, a[::-1])
        b = map(int, b[::-1])
        i, l = 0, min(len(a), len(b))
        c = list()
        count = 0
        while i < l:
            tmp = count + a[i] + b[i]
            if tmp >= 2:
                count = 1
                tmp -= 2
            else:
                count = 0
            c.append(tmp)
            i += 1
        c = c + a[l:] + b[l:]
        while count and l < len(c):
            c[l] += count
            if c[l] >= 2:
                count = 1
                c[l] -= 2
            else:
                count = 0
            l += 1
        if count == 1:
            c.append(1)
        return "".join(map(str,c[::-1]))
