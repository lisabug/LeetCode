#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'Yuanqin Lu'

class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0

        mapping = dict()
        for i in xrange(1,27):
            mapping[str(i)] = chr(ord('A')+i-1)
        state = [0 for i in xrange(len(s)+1)]
        state[0] = 1
        prev_char = '#'
        for i, c in enumerate(s,1):
            # decode this c
            if c in mapping:
                cur_decode = mapping[c]
                state[i] += state[i-1]
            # decode prev_char + c
            if prev_char+c in mapping:
                cur_decode = mapping[prev_char+c]
                state[i] += state[i-2]
            if not state[i]:
                return 0
            prev_char = c
        return state[-1]
