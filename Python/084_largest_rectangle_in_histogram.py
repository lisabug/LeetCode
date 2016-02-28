#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'Yuanqin Lu'

class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        stack = list()
        maxArea = 0
        heights.append(0)
        for k in xrange(len(heights)):
            while (stack and heights[k] < heights[stack[-1]]):
                area = heights[stack.pop()] * (k-stack[-1]-1 if stack else k)
                maxArea = max(maxArea, area)
            stack.append(k)

        return maxArea
