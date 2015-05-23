#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @author: Yuanqin Lu

def reverse(x):
    MAX = 0xFFFFFFFF/2
    MIN = -~0xFFFFFFFF/2

    if x is 0:
        return x

    if x > 0:
        signal = 1
    else:
        signal = -1

    strx = str(x)
    ans = 0

    for n in strx[::-1]:
        if not n.isdigit():
            continue
        if signal > 0 and (ans > MAX/10 or (ans == MAX/10 and int(n) > MAX % 10)):
            return 0
        if signal < 0 and (ans > MIN/10 or (ans == MIN/10 and int(n) > MIN % 10)):
            return 0
        ans = ans * 10 + int(n)

    return ans * signal
