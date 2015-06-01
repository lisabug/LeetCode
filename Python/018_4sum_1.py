#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @author: Yuanqin Lu

class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer[][]}
    def fourSum(self, nums, target):
        if len(nums) < 4:
            return []

        nums.sort()
        ret = []
        i = 0
        while i < len(nums) - 3:
            if nums[i] > target/4.0:
                break
            j = i + 1
            while j < len(nums) - 2:
                sum2 = nums[i] + nums[j]
                find_sum2 = target - sum2
                if sum2 > find_sum2:
                    break
                m = j + 1
                n = len(nums) - 1
                while m < n:
                    if nums[m] + nums[n] == find_sum2:
                        ret.append([nums[i], nums[j], nums[m], nums[n]])
                        while m < n and nums[m] == nums[m+1]: m += 1
                        while m < n and nums[n] == nums[n-1]: n -= 1
                        m += 1
                        n -= 1
                    elif nums[m] + nums[n] < find_sum2: m += 1
                    else: n -= 1
                while j < len(nums) - 2 and nums[j] == nums[j+1]: j += 1
                j += 1
            while i < len(nums) - 3 and nums[i] == nums[i+1]: i += 1
            i += 1

        return ret
