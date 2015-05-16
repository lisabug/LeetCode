#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @author: Yuanqin Lu

def findMedianSortedArrays(num1, num2):
    l = len(num1) + len(num2)
    if l % 2 == 0:
        return (findkth(num1, num2 , l/2-1) + findkth(num1, num2, l/2)) / 2.0
    else:
        return findkth(num1, num2, l/2)

def findkth(num1, num2, k):
    m = len(num1)
    n = len(num2)
    if m == 0:
        return num2[k]
    elif n == 0:
        return num1[k]
    ia, ib = m/2, n/2
    ma, mb = num1[ia], num2[ib]
    print "num1", num1
    print "num2", num2
    print "k", k

    if ia + ib < k:
        if ma < mb:
            return findkth(num1[ia+1:], num2, k-ia-1)
        else:
            return findkth(num1, num2[ib+1:], k-ib-1)
    else:
        if ma < mb:
            return findkth(num1, num2[:ib], k)
        else:
            return findkth(num1[:ia], num2, k)



if __name__ == '__main__':
    num1 = [1,2]
    num2 = [1,2]
    print findMedianSortedArrays(num1,num2)
