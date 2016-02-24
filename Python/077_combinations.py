#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'Yuanqin Lu'

class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        ans = []
        indices = range(1,k+1)

        def reset(index):
            if indices[index]>= n-k+1 + index:
                if index == 0:
                    indices[0] += 1
                    return
                reset(index-1)
                indices[index] = indices[index-1]+1
            else:
                indices[index]+=1

        while indices[0] <= n - k+1:
            ans.append(indices[:])
            indices[k-1] += 1
            if indices[k-1] > n:
                reset(k-1)

        return ans
