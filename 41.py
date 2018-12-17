# -*- coding: utf-8 -*-
"""
Created on Tue Feb 07 14:22:16 2017

@author: Jack

project euler question 41
"""
import numpy as np

def prev_pan(num="987654321"):
    """finds the previous n-pandigital number.
    automatically decreases n if needed"""
    num = str(num)[::-1]  # safety first
    staying = False
    b = len(num)
    base = "987654321"[9-b:]
    c = 1
    while c < b-1:
        if int(num[c]) > int(num[c-1]):
            staying = num[c+1:][::-1]
            pivot = int(num[c])-1
            #print staying, pivot
            break
        c+= 1
    if staying == False:
        return base[1:]
    
    while (str(pivot) in staying) is True:
        pivot -= 1
    staying += str(pivot)
    #print staying
    n = b
    while n > 0:
        if str(n) not in staying:
            staying += str(n)
        n-=1
    
    return staying

def is_prime(number):
    number = int(number)
    if number == 2:
        return True
    if number%2 == 0:
        return False
    for i in range(3, int(np.sqrt(number))+1, 2):
        if number%i == 0:
            return False
    return True

def solve_q(start="987654321"):
    """solves the question"""
    while is_prime(start) is False:
        #print start
        start = prev_pan(start)
    return start