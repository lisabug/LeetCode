#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'Yuanqin Lu'

class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: Set[str]
        :rtype: List[str]
        """
        def _dfs(s, path, ret):
            if _check(s):
                if not s:
                    ret.append(path[:-1])
                    return
                else:
                    for i in xrange(1, len(s)+1):
                        if s[:i] in wordDict:
                            _dfs(s[i:], path + s[:i] + ' ', ret)

        def _check(s):
            state = [False for _ in xrange(len(s)+1)]
            state[0] = True
            for i in xrange(1, len(s)+1):
                for j in xrange(i):
                    if state[j] and s[j:i] in wordDict:
                        state[i] = True
            return state[-1]

        ret = []
        _dfs(s, '', ret)

        return ret
