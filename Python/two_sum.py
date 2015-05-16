#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @author: Yuanqin Lu

def twoSum(self, num, target):
    hashed = {}
    for ind, value in enumerate(num):
        if hashed.has_key(target-value):
            return (hashed[target-value], ind+1)
        else:
            hashed[value] = ind+1
