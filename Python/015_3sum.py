#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @author: Yuanqin Lu

class Solution:
    # @param {integer[]} nums
    # @return {integer[][]}
    def threeSum(self, nums):
        nums_length = len(nums)
        if nums_length < 3:
            return []

        nums.sort()
        ans = []
        for i, num in enumerate(nums):
            if i == 0 or (i > 0 and i < nums_length - 2 and nums[i] != nums[i-1]):
                sum = -num
                m = i + 1
                n = nums_length - 1
                while m < n:
                    if nums[m] + nums[n] == sum:
                        ans.append([num, nums[m], nums[n]])
                        while m < n and nums[m] == nums[m+1]: m += 1
                        while m < n and nums[n] == nums[n-1]: n -= 1
                        m += 1
                        n -= 1
                    elif nums[m] + nums[n] < sum:
                        m+= 1
                    else:
                        n -= 1

        return ans

if __name__ == "__main__":
    s = Solution()
    nums = [-1, 0, 1, 2, -1, -4]
    print s.threeSum(nums)
