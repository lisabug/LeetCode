#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @author: Yuanqin Lu

class Solution:
    # @return an integer
    def romanToInt(self, s):
        roman_dic = {'I':1,'V':5,'X':10,'L':50, 'C':100,'D':500,'M':1000}
        strl = list(s)
        a = [roman_dic.get(v) for v in strl]
        ta = list(a)
        for i,v in enumerate(a):
            if i < len(a)-1 and a[i]<a[i+1]:
                ta[i]=-v
            else:
                ta[i]=v
        return sum(ta)


if __name__ == '__main__':
    s = Solution()
    print s.romanToInt("XIV")
