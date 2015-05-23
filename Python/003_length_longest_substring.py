#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @author: Yuanqin Lu

def lengthOfLongestSubstring(self, s):
    if s is None:
        return 0
    hash_table = {}
    max_len = 0
    start = 0
    for i, c in enumerate(s):
        if hash_table.has_key(c):
            if start <= hash_table[c]:
                start = hash_table[c] + 1
            hash_table[c] = i
        else:
            hash_table[c] = i
        tmp_len = i - start + 1
        if tmp_len > max_len:
            max_len = tmp_len

    return max_len
