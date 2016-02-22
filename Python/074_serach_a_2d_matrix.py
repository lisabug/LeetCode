#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'Yuanqin Lu'

class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix or not matrix[0]:
            return False
        m, n = len(matrix), len(matrix[0])
        i, j = 0, m*n-1
        while i <= j:
            mid = (i+j)/2
            if target > matrix[mid/n][mid%n]:
                i = mid + 1
            elif target < matrix[mid/n][mid%n]:
                j = mid - 1
            else:
                return True
        return False
