#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'Yuanqin Lu'

class Solution(object):
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        if not n:
            return [0]
        res = [0]
        for i in xrange(n):
            for j in xrange(len(res)-1, -1, -1):
                res.append(1 << i | res[j])
        return res
