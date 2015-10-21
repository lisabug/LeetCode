#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'Yuanqin Lu'

class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        m, n = len(s), len(p)
        i = j = 0
        si = 0
        sj = -1
        while i < m:
            if j < n and (s[i] == p[j] or p[j] == '?'):
                i += 1
                j += 1
            elif j < n and p[j] == '*':
                si = i
                sj = j
                # '*' match empty sequence
                j += 1
            elif sj >= 0:
                i = si + 1
                si += 1
                j = sj
            else:
                return False

        while j < n and p[j] == '*':
            j += 1

        return j == n
