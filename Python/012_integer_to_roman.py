#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @author: Yuanqin Lu
# "M", "MM", "MMM"
# "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"
# "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"
# "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"

def intToRoman(num):
    I = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]
    X = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
    C = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
    M = ["", "M", "MM", "MMM"]

    return M[num/1000] + C[(num%1000)/100] + X[(num%100)/10] + I[num%10]

if __name__ == '__main__':
    print intToRoman(18)
