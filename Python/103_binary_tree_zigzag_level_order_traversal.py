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
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        results = []
        prevLevel = [root]
        leftToRight = True
        while prevLevel:
            vals = []
            currLevel = []
            for node in prevLevel[::-1]:
                vals.append(node.val)
                if leftToRight:
                    if node.left:
                        currLevel.append(node.left)
                    if node.right:
                        currLevel.append(node.right)
                else:
                    if node.right:
                        currLevel.append(node.right)
                    if node.left:
                        currLevel.append(node.left)
            results.append(list(vals))
            prevLevel = list(currLevel)
            leftToRight = not leftToRight
        return results

