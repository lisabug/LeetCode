#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @author: Yuanqin Lu

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param {ListNode[]} lists
    # @return {ListNode}
    def mergeKLists(self, lists):
        if not list:
            return
        import heapq
        head = cur = ListNode(0)

        heap = [(l.val, l) for l in lists if l]
        heapq.heapify(heap)

        while heap:
            cur.next = heapq.heappop(heap)[1]
            cur = cur.next

            if cur.next:
                heapq.heappush(heap, (cur.next.val, cur.next))

        return head.next
