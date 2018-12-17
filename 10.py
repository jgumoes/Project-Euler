# -*- coding: utf-8 -*-
"""
Created on Tue Feb 07 18:07:55 2017

@author: Jack

project euler question 10
"""

def is_prime(number):
    if number == 2:
        return True
    if number%2 == 0:
        return False
    for i in range(3, int(number**.5)+1, 2):
        if number%i == 0:
            return False
    return True

num = 0
def solve_q(start=3):
    global num
    p_sum = 2
    while start < 2000000:
        p_sum+=start
        num = start
        start += 2
        while is_prime(start) is False:
            start+=2
    return p_sum
        