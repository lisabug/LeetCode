#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'Yuanqin Lu'

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """

        leftHead, leftNode, rightHead, rightNode = None, None, None, None
        while head:
            if head.val < x:
                if not leftHead:
                    leftHead = head
                    leftNode = head
                else:
                    leftNode.next = head
                    leftNode = leftNode.next
            else:
                if not rightHead:
                    rightHead = head
                    rightNode = head
                else:
                    rightNode.next = head
                    rightNode = rightNode.next
            head = head.next
        if leftNode:
            leftNode.next = rightHead
        if rightNode:
            rightNode.next = None
        return leftHead if leftHead else rightHead
