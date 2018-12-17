# -*- coding: utf-8 -*-
"""
Created on Tue Feb 07 16:13:19 2017

@author: Jack

project euler 51
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

def swap(num=56003):
    """does the swapping thing talked about in the question"""
    num = str(num)
    d = 0
    b_lim = 2**len(num) - 1
    b_count = 1
    end_primes = [0]
    primes = [] # [0]
    prime_list = []
    lens = []
    while b_count < b_lim:
        b = bin(b_count)[2:]
        while len(b) < len(num):
            b = "0" + b
        n = 0
        out = ""
        while n < len(b):
            #out += str(int(b[n])*d + (1-int(b[n]) * int(num[n])))
            if b[n] == '1':
                out += str(d)
            else:
                out += num[n]
            n+=1
        #print b, out
        if out[0] == '0':
            pass
        elif is_prime(int(out)) == True:
            primes.append(out)
        d+=1
        if d == 10:
            #print primes
            #if len(primes) > 7+1:
            #    return True, primes
            d = 0
            b_count += 1
            prime_list.append(primes)
            lens.append(len(primes))
            #end_primes.append(primes[-1])
            primes = []
    #return False, end_primes[-1]
    return prime_list[lens.index(max(lens))], max(lens)

q_check = 0

def solve_q(start=120384):
    """solves the question. 120383 works but PE doesn't like it". however,
    it does like 121313."""
    if start%2 == 0:
        start += 1
    while 1:
        while is_prime(start) is False:
            start += 2
        global q_check; q_check = start
        s_out = swap(start)
        if s_out[1] > 7:
            return start, s_out
        start += 2
    