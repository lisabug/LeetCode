#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @author: Yuanqin Lu

class Solution:
    # @param {string[]} strs
    # @return {string}
    def longestCommonPrefix(self, strs):
        if len(strs) == 0:
            return ""

        strs_number = len(strs)
        min_length = len(strs[0])

        for str in strs:
            tmp_length = len(str)
            if tmp_length < min_length:
                min_length = tmp_length

        lcp = ""
        end_flag = False
        for i in xrange(min_length):
            tmp_char = strs[0][i]
            for j in xrange(1, strs_number):
                if tmp_char != strs[j][i]:
                    end_flag = True
                    break

            if end_flag:
                break
            lcp += tmp_char

        return lcp

if __name__ == '__main__':
    s = Solution()
    strs = ["aaa", "aab", "aacd"]
    print s.longestCommonPrefix(strs)
