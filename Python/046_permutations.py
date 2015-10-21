#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'Yuanqin Lu'

class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ret = []
        # sort list
        nums.sort()
        # add a new copy of nums to return list, so use list() function
        ret.append(list(nums))
        i = len(nums) - 1

        while i > 0:
            # find first a[i] < a[i+1]
            if nums[i-1] <= nums[i]:
                j = len(nums) - 1
                minMax = max(nums)
                while j > i-1:
                    # find the minmum a[j] > a[i]
                    if nums[j] > nums[i-1] and nums[j] <= minMax:
                        ind = j
                        minMax = nums[j]
                        j -= 1

                    else:
                        j -= 1
                # swap
                nums[ind], nums[i-1] = nums[i-1], nums[ind]
                nums = nums[:i] + nums[i:][::-1]
                ret.append(list(nums))
                i = len(nums) - 1
            else:
                i -= 1

        return ret

if __name__ == '__main__':
    s = Solution()
    nums = [2,1,3]
    print(s.permute(nums))
