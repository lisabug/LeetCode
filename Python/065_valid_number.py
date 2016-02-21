#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'Yuanqin Lu'

class Solution(object):
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = s.strip()
        idxPoint, idxExp, isNum = -1, -1, False
        i, l =0, len(s)
        while i < l:
            if '0' <= s[i] <= '9':
                i += 1
                isNum = True
                continue
            elif s[i] == '+' or s[i] == '-':
                if i == 0 or i == idxExp + 1:
                    i += 1
                    continue
                else:
                    return False
            elif s[i] == '.':
                if idxPoint == -1:
                    idxPoint = i
                    i += 1
                    continue
                else:
                    return False
            elif s[i] == 'e':
                if idxExp == -1 and isNum:
                    idxExp = i
                    idxPoint = i
                    i += 1
                    isNum = False
                    continue
                else:
                    return False
            else:
                return False
        return isNum
