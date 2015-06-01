#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @author: Yuanqin Lu

class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer[][]}
    def fourSum(self, nums, target):
        if not nums:
            return []
        nums.sort()

        def ksum(num, k, target):
            i = 0
            result = set()
            if k == 2:
                j = len(num) - 1
                while i < j:
                    if num[i] + num[j] == target:
                        result.add((num[i], num[j]))
                        i += 1
                        j -= 1
                    elif num[i] + num[j] < target: i += 1
                    else: j -= 1
            else:
                while i < len(num) - k + 1:
                    newtarget = target - num[i]
                    subresult = ksum(num[i+1:], k-1, newtarget)
                    if subresult:
                        result = result | set((num[i],) + nr for nr in subresult)
                    i += 1
            return result

        return [list(t) for t in ksum(nums, 4, target)]
