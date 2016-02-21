#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'Yuanqin Lu'

class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        rootStack = []
        for p in path.split('/'):
            if p == "..":
                if rootStack:
                    rootStack.pop()
            elif p == "." or p == "/" or p == "":
                continue
            else:
                rootStack.append(p)
        if not rootStack:
            rootStack.append("")
        slashes = ["/"] * len(rootStack)
        return "".join([s for pair in zip(slashes, rootStack) for s in pair])
