#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'Yuanqin Lu'

class Solution(object):
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        m = len(s1)
        n = len(s2)
        l = len(s3)
        if m + n != l:
            return False
        state = [[False for i in xrange(n+1)] for i in xrange(m+1)]
        state[0][0] = True

        for i, c3 in enumerate(s3,1):
            for j in xrange(max(0, i-n), min(i+1, m+1)):
                state[j][i-j] = (state[j-1][i-j] and s1[j-1] == s3[i-1]) or (state[j][i-j-1] and s2[i-j-1] == s3[i-1])

        return state[-1][-1]

if __name__ == '__main__':
    s = Solution()
    s1 = ""
    s2 = ""
    s3 = "a"
    print s.isInterleave(s1,s2,s3)
