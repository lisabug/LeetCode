#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'Yuanqin Lu'

# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """
        if not intervals:
            return [newInterval]
        retIntervals = list()
        for i, interval in enumerate(intervals):
            if interval.end < newInterval.start:
                retIntervals.append(interval)
            elif interval.start > newInterval.end:
                retIntervals.append(newInterval)
                return retIntervals + intervals[i:]
            else:
                newInterval.start = min(newInterval.start, interval.start)
                newInterval.end = max(newInterval.end, interval.end)
        retIntervals.append(newInterval)
        return retIntervals

