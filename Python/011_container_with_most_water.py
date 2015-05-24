#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @author: Yuanqin Lu

def maxArea(height):
    max_area = 0
    i = 0
    j = len(height) - 1
    while i < j:
        max_area = max(max_area, (j-i)*min(height[i], height[j]))
        if height[i] < height[j]:
            i += 1
        else:
            j -= 1

    return max_area


if __name__ == '__main__':
    print maxArea([1,1,1,1,1,1])
    print maxArea([2,1])
