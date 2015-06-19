#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'Yuanqin Lu'

class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer[]}
    def searchRange(self, nums, target):
        if not nums:
            return [-1,-1]

        left = 0
        right = len(nums) - 1
        leftIndex = -1
        rightIndex = -1
        while left <= right:
            mid = (left+right)/2
            if nums[mid] == target and (mid==0 or (mid > 0 and nums[mid-1] != nums[mid])):
                leftIndex = mid
                break
            elif target < nums[mid] or (target == nums[mid] and mid > 0 and nums[mid-1] == nums[mid]):
                right = mid - 1
            else:
                left = mid + 1
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left+right)/2
            if nums[mid] == target and (mid == len(nums) - 1 or (mid < len(nums)-1 and nums[mid] != nums[mid+1])):
                rightIndex = mid
                break
            elif target > nums[mid] or (target == nums[mid] and mid < len(nums) - 1 and nums[mid] == nums[mid+1]):
                left = mid + 1
            else:
                right = mid - 1

        return [leftIndex, rightIndex]
