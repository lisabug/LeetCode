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
    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        if not root:
            return
        self.prev = TreeNode(-0xFFFFFFFF)
        self.first, self.second = None, None
        self.helper(root)
        self.first.val, self.second.val = self.second.val, self.first.val

    def helper(self, root):
        if not root:
            return
        self.helper(root.left)
        if not self.first and self.prev.val >= root.val:
            self.first, self.second = self.prev, root
        if self.first and self.prev.val >= root.val:
            self.second = root
        self.prev = root
        self.helper(root.right)
