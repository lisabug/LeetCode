#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'Yuanqin Lu'

class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        ret = dict()
        for item in strs:
            key = ''.join(sorted(item))
            ret.setdefault(key, []).append(item)

        return [sorted(v) for v in ret.values()]
