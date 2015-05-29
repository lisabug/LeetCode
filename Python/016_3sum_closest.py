#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @author: Yuanqin Lu

class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer}
    def threeSumClosest(self, nums, target):
        if len(nums) < 3:
            return 0

        nums.sort()
        print nums
        result = nums[0] + nums[1] + nums[2]
        for i, num in enumerate(nums):
            if i > len(nums) - 2:
                break

            j = i + 1
            k = len(nums) - 1

            while j < k:
                tmp_sum = nums[i] + nums[j] + nums[k]
                if tmp_sum == target: return tmp_sum
                if abs(tmp_sum - target) < abs(result - target):
                    result = tmp_sum
                if tmp_sum < target: j += 1
                if tmp_sum > target: k -= 1

        return result

if __name__ == '__main__':
    s = Solution()
    nums = [0, 2, 1, -3]
    target = 1
    print s.threeSumClosest(nums, target)


