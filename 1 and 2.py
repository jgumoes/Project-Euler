# -*- coding: utf-8 -*-
"""
Created on Mon Jan 09 14:56:41 2017

@author: Jack

doing questions on projecteuler.net
"""

import numpy as np

def q1():
    ans = 0
    c = 1
    
    while c*3 < 1000:
        ans += c*3
        c+=1 
    
    print c
    c = 1
    
    while c*5 < 1000:
        ans += c*5
        c+=1     
    
    print c
    c = 1
    
    while c*5*3 < 1000:
        ans -= c*3*5
        c+=1
    print c
    return ans

def q2():
    n = [1,2]
    ans = 0
    while n[1] <= 4000000:
        n0 = n[0]; n1 = n[1]
        if n1%2 == 0:
            ans = ans + n1
        n = [n1, n0 + n1]

    return ans, n

def q4():
    pals = np.array([])
    numb = 999*999
    
print q4()

        