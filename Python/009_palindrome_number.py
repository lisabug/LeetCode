#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @author: Yuanqin Lu

def isPalindrome(x):
    if x < 0 or (x != 0 and x % 10 == 0):
        return False

    sum = 0
    while x > sum:
        sum = sum*10 + x % 10
        x = x / 10

    return x == sum or x == sum / 10

if __name__ == '__main__':
    print isPalindrome(121)
    print isPalindrome(1221)
    print isPalindrome(122)

