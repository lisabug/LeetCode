#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'Yuanqin Lu'

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        # get length
        if not head:
            return None
        tmp = head
        length = 0
        while tmp:
            length += 1
            tmp = tmp.next
        k %= length
        if k == 0:
            return head
        tmp = head
        ret = None
        for i in xrange(1, length):
            if i == length-k:
                ret = tmp.next
                tmp.next = None
                tmp = ret
            else:
                tmp = tmp.next
        tmp.next = head
        return ret

