#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'Yuanqin Lu'

class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        hashTable = dict()
        count = len(t)
        for c in t:
            hashTable[c] = hashTable.get(c, 0) + 1
        start, minStart = 0,0
        minLength = len(s) + 1
        for end, c in enumerate(s):
            if hashTable.get(c,0) > 0:
                count -= 1
            hashTable[c] = hashTable.get(c, 0) - 1
            while count == 0:
                if end - start < minLength:
                    minStart = start
                    minLength = end - start
                hashTable[s[start]] = hashTable.get(s[start], 0) + 1
                if hashTable[s[start]] > 0:
                    count += 1
                start += 1

        return s[minStart:minStart+minLength+1] if minLength <= len(s) else ""
