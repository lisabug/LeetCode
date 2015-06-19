#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'Yuanqin Lu'

class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer}
    def searchInsert(self, nums, target):
        if not nums:
            return

        index = -1
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left+right)/2
            if target == nums[mid]: return mid
            elif target < nums[mid]: right = mid - 1
            else: left = mid + 1

        return (left+right)/2 + 1
