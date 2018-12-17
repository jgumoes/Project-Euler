# -*- coding: utf-8 -*-
"""
Created on Tue Jan 24 13:53:43 2017

@author: Jack

project euler question 3, find the largest prime factor of 600851475143
"""
import numpy as np


def is_prime(number):
    if number == 2:
        return True
    if number%2 == 0:
        return False
    for i in range(3, int(np.sqrt(number))+1, 2):
        if number%i == 0:
            return False
    return True

def q3():
    num = 600851475143
    c = 2
    ans = np.array([], dtype=int)
    while num > 1:
        print num
        if is_prime(c) is True:
            if num%c == 0:
                ans = np.append(ans, [c])
                num = num/c
            else:
                c+=1
        else:
            c+=1
    return ans