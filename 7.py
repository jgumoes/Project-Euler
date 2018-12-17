# -*- coding: utf-8 -*-
"""
Created on Thu Jan 26 12:35:31 2017

@author: Jack

project euler question 7
"""

import numpy as np

def is_prime(num):
    """Checks if number num is a prime number. 2, 3, and 5 won't be caught.
    num must be odd"""
    l = np.linspace(3, num/2 +1, num/2 -1, dtype=int)
    ans = num%l
    for i in ans:
        if i == 0:
            return False
    return True

def find_prime(term):
    """finds 10,001st prime"""
    c = 4
    num = 7
    while c != term: #10001:
        num+=2
        if is_prime(num) == True:
            c+=1
    return c, num