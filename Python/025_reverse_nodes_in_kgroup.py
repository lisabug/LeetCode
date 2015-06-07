#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @author: Yuanqin Lu

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param {ListNode} head
    # @param {integer} k
    # @return {ListNode}
    def reverseKGroup(self, head, k):
        if not head or k <= 1:
            return head

        ret = ListNode(0)
        ret.next = head
        pre = ret
        while True:
            # whether sublist's length is shorter than k
            head = pre.next
            for i in xrange(k):
                if not head:
                    return ret.next
                head = head.next
            head = pre.next.next
            tail = pre.next
            # reverse
            prepre = ListNode(0)
            for i in xrange(k-1):
                if i == 0:
                    prepre = tail
                pre.next = head
                prepre.next = head.next
                head.next = tail
                tmp = head
                head = prepre.next
                tail = tmp
            pre = prepre

if __name__ == '__main__':
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)

    s = Solution()
    s.reverseKGroup(head, 4)
