#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @author: Yuanqin Lu

def addTwoNumbers(self, l1, l2):
    head = ListNode(0)
    tmp = head

    while l1 is not None and l2 is not None:
        tmp.val = l1.val + l2.val
        tmp.next = ListNode(0)
        tmp = tmp.next
        l1 = l1.next
        l2 = l2.next

    if l1 is not None:
        tmp.val = l1.val
        tmp.next = l1.next
    elif l2 is not None:
        tmp.val = l2.val
        tmp.next = l2.next

    c = 0
    tmp = head
    while tmp.next:
        tmp.val += c
        if tmp.val >= 10:
            tmp.val -= 10
            c = 1
        else:
            c = 0
        pre = tmp
        tmp = tmp.next

    if c == 1:
        tmp.val += 1
        if tmp.val >= 10:
            tmp.val -= 10
            tmp.next = ListNode(1)
            tmp = tmp.next
    if tmp.val == 0:
        pre.next = None


    return head
