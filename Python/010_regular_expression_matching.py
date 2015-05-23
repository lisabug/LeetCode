#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @author: Yuanqin Lu
#Some examples:
#isMatch("aa","a") → false
#isMatch("aa","aa") → true
#isMatch("aaa","aa") → false
#isMatch("aa", "a*") → true
#isMatch("aa", ".*") → true
#isMatch("ab", ".*") → true
#isMatch("aab", "c*a*b") → true

"""
Recursive resolution, TLE
def isMatch(s, p):
    if (len(p) == 0):
        return (len(s) == 0)

    if (len(p) > 1 and p[1] == '*'):
        return (isMatch(s, p[2::]) or (len(s) > 0 and (s[0] == p[0] or p[0] == '.') and isMatch(s[1::], p)))
    else:
        if len(s) == 0:
            return False
        if s[0] == p[0] or p[0] == '.':
            return isMatch(s[1::], p[1::])
        else:
            return False
"""
# DP solution
def isMatch(s, p):
    if len(p) == 0:
        return len(s) == 0

    ans = [[False for x in xrange(len(p)+1)] for x in xrange(len(s)+1)]
    ans[0][0] = True

    for i in xrange(1, len(p)):
        ans[0][i+1] = ans[0][i-1] and p[i] == '*'

    for i in xrange(len(s)):
        for j in xrange(len(p)):
            if p[j] != '*':
                ans[i+1][j+1] = ans[i][j] and (s[i] == p[j] or p[j] == '.')
            else:
                ans[i+1][j+1] = (j > 0 and ans[i+1][j-1]) or ans[i+1][j] or (ans[i][j+1] and j > 0 and (p[j-1] == '.' or s[i] == p[j-1]))

    return ans[-1][-1]



if __name__ == '__main__':
    print isMatch("aa","a")
    print isMatch("aa","aa")
    print isMatch("aaa","aa")
    print isMatch("aa", "a*")
    print isMatch("aa", ".*")
    print isMatch("ab", ".*")
    print isMatch("aab", "c*a*b")
    print isMatch("aaa","aaaa")
    print isMatch("aaac",".*ac")
