#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'Yuanqin Lu'

class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: Set[str]
        :rtype: int
        """
        import string
        front, back = set([beginWord]), set([endWord])
        wordList -= front
        wordList -= back
        width = len(beginWord)
        length = 2
        chars = list(string.lowercase)
        while front:
            new_front = set()
            for phrase in front:
                for i in xrange(width):
                    for c in chars:
                        nw = phrase[:i] + c + phrase[i+1:]
                        if nw in back:
                            return length
                        if nw in wordList:
                            new_front.add(nw)
            front = new_front
            if len(front) > len(back):
                front, back = back, front
            wordList -= front
            length += 1
        return 0

if __name__ == '__main__':
    s = Solution()
    bWord = 'hot'
    eWord = 'dog'
    wordList = set(['hot', 'dog' ])
    print s.ladderLength(bWord, eWord, wordList)
