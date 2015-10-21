#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'Yuanqin Lu'

class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n == 1:
            return 0

        maxIndex = 0
        lastIndex = 0
        nextIndex = 0
        numJump = 0
        while True:
            # find next index of jump
            ## the maxium of current jump
            maxJump = nums[lastIndex]
            numJump += 1
            if maxJump + lastIndex >= n-1:
                break
            i = 1
            while i <= maxJump:
                tmpMaxIndex = lastIndex + i + nums[lastIndex+i]
                if tmpMaxIndex > maxIndex:
                    maxIndex = tmpMaxIndex
                    nextIndex = lastIndex + i
                i += 1

            lastIndex = nextIndex


        return numJump
