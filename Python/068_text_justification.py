#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'Yuanqin Lu'

class Solution(object):
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        i, N, result = 0, len(words), []
        while i < N:
            oneLine, j, curWidth, positionNum, spaceNum = [words[i]], i+1, len(words[i]), 0, maxWidth-len(words[i])
            while j < N and curWidth + 1 + len(words[j]) <= maxWidth:
                oneLine.append(words[j])
                curWidth += len(words[j]) + 1
                spaceNum -= len(words[j])
                positionNum, j = positionNum+1, j+1
            i = j
            # decide layout of oneline
            if i < N and positionNum:
                spaces = [" " * (spaceNum / positionNum + (k < spaceNum % positionNum)) for k in xrange(positionNum)] + [""]
            else:
                spaces = [" "] * positionNum + [" "*(maxWidth-curWidth)]
            result.append("".join([s for pair in zip(oneLine, spaces) for s in pair]))

        return result

