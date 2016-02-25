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
        if not head or not head.next:
            return head

        retNode, saveNode, prevNode, currNode, nextNode = None, None, None, head, head.next
        while True:
            if (not prevNode or prevNode.val != currNode.val) and (not nextNode or currNode.val != nextNode.val):
                if not retNode:
                    saveNode = currNode
                    retNode = saveNode
                else:
                    saveNode.next = currNode
                    saveNode = saveNode.next
            if not nextNode: break
            prevNode, currNode, nextNode = currNode, nextNode, nextNode.next
        if saveNode: saveNode.next = None
        return retNode
