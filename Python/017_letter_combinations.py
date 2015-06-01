#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @author: Yuanqin Lu

class Solution:
    # @param {string} digits
    # @return {string[]}
    keyboard = {'2':'abc', '3':'def', '4':'ghi', '5':'jkl', '6':'mno', '7': 'pqrs', '8':'tuv', '9':'wxyz', '0':' '}
    def letterCombinations(self, digits):
        if len(digits) == 0:
            return []
        return self._dfs(digits)

    def _dfs(self, digits):
        if len(digits) == 1:
            ret = []
            for char in self.keyboard[digits[0]]:
                ret.append(char)
            return ret
        else:
            ret = []
            for char in self.keyboard[digits[0]]:
                for left_char in self._dfs(digits[1:]):
                    ret.append(char+left_char)
            return ret

if __name__ == "__main__":
    s = Solution()
    number = "23"
    print s.letterCombinations(number)
