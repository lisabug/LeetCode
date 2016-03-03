#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'Yuanqin Lu'

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        results = []
        prevLevel = [root]
        while prevLevel:
            currLevel = []
            vals = []
            for node in prevLevel:
                vals.append(node.val)
                if node.left:
                    currLevel.append(node.left)
                if node.right:
                    currLevel.append(node.right)
            prevLevel = list(currLevel)
            results.append(list(vals))
        return results
