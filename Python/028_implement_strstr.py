#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @author: Yuanqin Lu

class Solution:
    # @param {string} haystack
    # @param {string} needle
    # @return {integer}
    def strStr(self, haystack, needle):
        return self._kmpSearch(haystack, needle)

    def _getNext(self, p):
        if len(p) == 0:
            return
        next = [0 for x in xrange(len(p))]
        next[0] = -1
        k = -1
        i = 0
        while i < len(p) - 1:
            if k == -1 or p[i] == p[k]:
                i += 1
                k += 1
                if p[i] != p[k]:
                    next[i] = k
                else:
                    next[i] = next[k]
            else:
                k = next[k]
        return next

    def _kmpSearch(self, s, p):
        next = self._getNext(p)
        lenS = len(s)
        lenP = len(p)
        i = j = -1
        while i < lenS and j < lenP:
            if j == -1 or s[i] == p[j]:
                i += 1
                j += 1
            else:
                j = next[j]

        if j == lenP:
            return i - j
        else:
            return -1
