#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'Yuanqin Lu'

class Solution(object):
    def minCut(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s == s[::-1]: return 0
        for i in range(1, len(s)):
            if s[:i] == s[:i][::-1] and s[i:] == s[i:][::-1]:
                return 1
        n = len(s)
        cut = [i for i in xrange(n)]
        i = 1
        while i < n:
            j = -1
            while j < i:
                subString = s[j+1:i+1]
                reversedStr = subString[::-1]
                if subString == reversedStr:
                    if j == -1:
                        cut[i] = 0
                        break
                    else:
                        cut[i] = min(cut[i], cut[j] + 1)
                j += 1
            i += 1
        return cut[-1]

