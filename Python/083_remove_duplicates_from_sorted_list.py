#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'Yuanqin Lu'

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None

        prev, curr = head, head.next
        while curr:
            if prev.val == curr.val:
                curr = curr.next
            else:
                prev.next = curr
                prev = curr
        prev.next = None
        return head
