#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'Yuanqin Lu'

class Solution:
    # @param {integer[]} candidates
    # @param {integer} target
    # @return {integer[][]}
    def combinationSum2(self, candidates, target):
        def _dfs(candidates, target, ind):
            if ind >= len(candidates) or candidates[ind] > target:
                return []
            else:
                ret = []
                i = ind
                while i < len(candidates):
                    if target-candidates[i] == 0:
                        ret.append([candidates[i]])
                        break
                    else:
                        tmp = _dfs(candidates, target-candidates[i], i+1)
                        if tmp:
                            for t in tmp:
                                ret.append([candidates[i]]+t)
                    while i < len(candidates)-1 and candidates[i] == candidates[i+1]: i+= 1
                    i += 1

                return ret

        candidates.sort()
        return _dfs(candidates, target, 0)
