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
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        def equal(p, q):
            if p and q:
                return p.val == q.val and equal(p.left, q.left) and equal(p.right, q.right)
            elif not p and not q:
                return True
            else:
                return False
        return equal(p,q)
