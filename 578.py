# -*- coding: utf-8 -*-
"""
Created on Sun Feb 05 21:10:31 2017

@author: Jack

project euler problem 578
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

def find_factors(num):
    c = 2
    ans = [] #np.array([])
    indice = 0
    while num > 1:
        print num
        if is_prime(c) is True:
            if num%c == 0:
                #ans = np.append(ans, [c])
                num = num/c
                indice+=1
            else:
                ans.append([c, indice])
                c+=1
                indice = 0
        else:
            c+=1
    return ans