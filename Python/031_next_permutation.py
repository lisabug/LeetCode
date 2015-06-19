#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'Yuanqin Lu'

class Solution:
    # @param {integer[]} nums
    # @return {void} Do not return anything, modify nums in-place instead.
    def nextPermutation(self, nums):
        if not nums or len(nums) == 1:
            return
        l = len(nums)-1
        # find first nums[i] < nums[i+1]
        while l > 0:
            if nums[l] > nums[l-1]:
                break
            l -= 1
        print l
        if l == 0:
            nums.sort()
        else:
            i = len(nums)-1
            while i > l-1:
                if nums[i] > nums[l-1]:
                    nums[i], nums[l-1] = nums[l-1], nums[i]
                    break
                i -= 1
            # reverse
            j = len(nums) -1
            while l < j:
                nums[l], nums[j] = nums[j], nums[l]
                l += 1
                j -= 1

if __name__ == '__main__':
    s = Solution()
    nums = [3,2,1]
    nums1 = [1, 2, 3]
    s.nextPermutation(nums)
    print nums
