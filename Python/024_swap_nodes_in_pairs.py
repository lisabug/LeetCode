#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @author: Yuanqin Lu

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param {ListNode} head
    # @return {ListNode}
    def swapPairs(self, head):
        if not head or not head.next:
            return head

        ret = ListNode(0)
        ret.next = head
        pre = ret
        while head and head.next:
            pre.next = head.next
            head.next = head.next.next
            pre.next.next = head
            pre = head
            head = head.next

        return ret.next
