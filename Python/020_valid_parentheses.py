#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @author: Yuanqin Lu

class Solution:
    # @param {string} s
    # @return {boolean}
    def isValid(self, s):
        if len(s) % 2 == 1:
            return False
        paren = {"(":")", "{":"}", "[":"]"}
        stack = []
        for p in s:
            if p in paren:
                stack.append(p)
            else:
                if not stack or paren[stack.pop()] != p:
                    return False

        if stack:
            return False
        return True
