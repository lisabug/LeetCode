#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @author: Yuanqin Lu

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param {ListNode} l1
    # @param {ListNode} l2
    # @return {ListNode}
    def mergeTwoLists(self, l1, l2):
        def _mergeTwoLists(l1, l2):
            if not l1:
                return l2
            elif not l2:
                return l1

            if l1.val < l2.val:
                l1.next = _mergeTwoLists(l1.next, l2)
                return l1
            else:
                l2.next = _mergeTwoLists(l1, l2.next)
                return l2

        return _mergeTwoLists(l1,l2)
