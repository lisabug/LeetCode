#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @author: Yuanqin Lu

def atoi(self, str):
    MAX_INT = 0xFFFFFFFF/2
    MIN_INT = -~0xFFFFFFFF/2
    if str is None or len(str) == 0:
        return 0

    str = str.strip()

    n = 0
    sign = 1
    if str[0] == '+':
        str = str[1:]
    elif str[0] == '-':
        sign = -1
        str = str[1:]

    for c in str:
        if not c.isdigit():
            break

        if sign > 0 and (n > MAX_INT / 10 or (n == MAX_INT / 10 and int(c) > MAX_INT % 10)):
            return MAX_INT
        elif sign < 0 and ( n > MIN_INT / 10 or (n == MIN_INT / 10 and int(c) > MIN_INT % 10)):
            return -MIN_INT
        n = n * 10 + int(c)

    return sign*n
