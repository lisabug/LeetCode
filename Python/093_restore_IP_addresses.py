#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'Yuanqin Lu'

class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        def helper(res, tmp, s, start):
            if start == len(s) and len(tmp) == 4:
                res.append('.'.join(map(str, tmp)))
            for end in xrange(start, len(s)):
                num = int(s[start:end+1])
                if 0 <= num <= 255 and not (s[start] == '0' and end != start):
                    helper(res, tmp + [num], s, end+1)
        if not s or len(s) > 12 or len(s) < 4:
            return []
        res = []
        helper(res, [], s, 0)
        return res
