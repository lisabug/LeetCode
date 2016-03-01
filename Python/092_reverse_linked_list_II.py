#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'Yuanqin Lu'

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        if not head or not head.next or m == n:
            return head
        reverseTail, prevReverse, prev, curr = None, None, None, head
        i = 1
        while curr:
            if i <= m:
                if i == m-1:
                    prevReverse = curr
                if i == m:
                    reverseTail = curr
                prev, curr = curr, curr.next
            elif i < n:
                tmp, curr.next = curr.next, prev
                prev, curr = curr, tmp
            elif i == n:
                reverseTail.next = curr.next
                curr.next = prev
                if prevReverse:
                    prevReverse.next = curr
                else:
                    head = curr
                break
            i += 1

        return head

