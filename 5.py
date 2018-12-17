# -*- coding: utf-8 -*-
"""
Created on Thu Jan 26 12:11:47 2017

@author: Jack

project euler question 5

"""


def check(num):
    c = 20
    while c > 0:
        if num%c != 0:
            print c
        c-=1
    return num