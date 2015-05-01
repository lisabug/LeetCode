#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @author: Yuanqin Lu

def longestPalindrome(s):
    # construct special structure to find solution easily
    ss = "$#" + reduce(plus_symbol, s) + "#"
    m = id = 1
    p = [1] * len(ss)

    # calculate the longest palindrome string: index of center and the length
    for (i, c) in enumerate(ss):
        if i < m:
            p[i] = min(m-i, p[2*id-i])
        while i+p[i] < len(ss) and i - p[i] >= 0 and ss[i+p[i]] == ss[i-p[i]]:
            p[i] += 1
        if p[i] > p[id]:
            id = i
            m = i + p[i]

    # find longest palindrome substring
    tmp_longest = ss[id-p[id]+1:id+p[id]+1]
    longest = filter(discard_symbol, tmp_longest)

    return longest


def plus_symbol(p, q):
    return p + "#" + q

def discard_symbol(s):
    return s != "#" and s != "$"

print longestPalindrome("a")
