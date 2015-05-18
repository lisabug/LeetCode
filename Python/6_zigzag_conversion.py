#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @author: Yuanqin Lu

def convert(s, numRows):
    if s is None or len(s) == 0 or numRows == 1:
        return s

    tmpRows = []
    for i in xrange(numRows):
        tmpRows.append([])

    for i, c in enumerate(s):
        index = numRows - 1 - abs(i % (2 * (numRows-1)) - (numRows-1))
        tmpRows[index].append(c)

    str = ""
    for row in tmpRows:
        str += "".join(row)
    return str

print convert("PAYPALISHIRING", 3)
