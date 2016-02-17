#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'Yuanqin Lu'

class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix or not matrix[0]:
            return list()
        direction = 1
        upper = left = 0
        below = len(matrix)
        right = len(matrix[0])
        ans = list()
        i = j = 0
        while i >= upper and i < below and j >= left and j < right:
            ans.append(matrix[i][j])
            if direction == 1:
                # go right
                j += 1
                if j == right:
                    direction = 2
                    upper += 1
                    j -= 1
                    i += 1
            elif direction == 2:
                # go down
                i += 1
                if i == below:
                    direction = 3
                    right -= 1
                    i -= 1
                    j -= 1
            elif direction == 3:
                # go left
                j -= 1
                if j == left - 1:
                    direction = 4
                    below -= 1
                    j += 1
                    i -= 1
            else:
                # go up
                i -= 1
                if i == upper - 1:
                    direction = 1
                    left += 1
                    i += 1
                    j += 1
        return ans
