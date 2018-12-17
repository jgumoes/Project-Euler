# -*- coding: utf-8 -*-
"""
Created on Sun Oct  1 13:21:43 2017

@author: Jack
"""


def i_need_a_function():
    """I need a function for a quick bail"""
    a = 1
    b = 1
    c = 1
    
    while a< 1000:
        while b < 1000:
            c = (b**2 + a**2)**0.5
            if c-int(c) == 0:
                if a+b+c == 1000:
                    print("a = %d" % a)
                    print("b = %d" % b)
                    print("c = %d" % c)
                    return a*b*c
            b+=1
            print("b is now %d \t and a is now %d" % (b, a))
        a+=1
        b=1
        #print("a is now %d" % a)

i_need_a_function()