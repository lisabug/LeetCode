#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'Yuanqin Lu'

class Solution:
    # @param {string} s
    # @return {integer}
    def longestValidParentheses(self, s):
        if not s:
            return 0

        stack = []
        cLen = 0
        mLen = 0
        last = -1
        for i, c in enumerate(s):
            if c == '(':
                stack.append(i)
            else:
                if stack:
                    tmp = stack.pop()
                    if stack:
                        cLen = i - stack[-1]
                    else:
                        cLen = i - last
                    mLen = max(mLen, cLen)
                else:
                    last = i

        return mLen

if __name__ == '__main__':
    s = Solution()
    t = '()'
    print s.longestValidParentheses(t)
