#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @author: Yuanqin Lu

class Solution:
    # @param {integer} n
    # @return {string[]}
    def generateParenthesis(self, n):
        if n == 0:
            return []
        if n == 1:
            return ['()']

        def helper(s, ln, rn):
            current_ret = []
            if 0 < ln < rn:
                current_ret += helper(s+'(', ln-1, rn)
                current_ret += helper(s+')', ln, rn-1)
            if ln == 0 and rn > 0:
                s += ')'*rn
                return [s]
            if ln == rn and ln != 0:
                current_ret += helper(s+'(', ln-1,rn)
            return current_ret

        ret = helper('(', n-1, n)

        return ret
