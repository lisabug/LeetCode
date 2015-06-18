#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'Yuanqin Lu'

class Solution:
    # @param {string} s
    # @param {string[]} words
    # @return {integer[]}
    def findSubstring(self, s, words):
        if not s or not words:
            return []

        lWord = len(words[0])
        nWords = len(words)
        lString = len(s)
        dic = {}
        for word in words:
            if word in dic:
                dic[word] += 1
            else:
                dic[word] = 1
        ans = []
        for i in xrange(lWord):
            subdic = {}
            count = 0
            left = i
            for j in xrange(i, lString-lWord+1, lWord):
                print left
                tWord = s[j:j+lWord]
                if tWord in dic:
                    if tWord in subdic:
                        subdic[tWord] += 1
                    else:
                        subdic[tWord] = 1
                    count += 1
                    while subdic[tWord] > dic[tWord]:
                        subdic[s[left:left+lWord]] -= 1
                        count -= 1
                        left += lWord
                    if count == nWords:
                        ans.append(left)
                else:
                    subdic = {}
                    count = 0
                    left = j + lWord
        return ans

if __name__ == '__main__':
    s = Solution()
    string = 'barfoothefoobarman'
    words = ["foo", "bar"]
    print s.findSubstring(string, words)
