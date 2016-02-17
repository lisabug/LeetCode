#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'Yuanqin Lu'

# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        if not intervals:
            return list()
        intervals.sort(key=lambda x:x.start)
        ret = list()
        pre = intervals[0]
        for nxt in intervals:
            if pre.end < nxt.start:
                ret.append(pre)
                pre = nxt
            elif pre.end <= nxt.end:
                pre.end = nxt.end
        ret.append(pre)

        return ret
