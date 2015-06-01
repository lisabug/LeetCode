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
    # @param {integer} n
    # @return {ListNode}
    def removeNthFromEnd(self, head, n):
        if not head:
            return None

        head1 = head
        head2 = head
        for i in xrange(n):
            head1 = head1.next
            if not head1:
                return head.next
        while head1.next:
            head1 = head1.next
            head2 = head2.next

        head2.next = head2.next.next
        return head

