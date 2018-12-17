# -*- coding: utf-8 -*-
"""
Created on Tue Feb 07 18:19:03 2017

@author: Jack

project euler question 60
"""

def is_prime(number):
    number = int(number)
    if number == 2:
        return True
    if number%2 == 0:
        return False
    for i in range(3, int(number**.5)+1, 2):
        if number%i == 0:
            return False
    return True

def conc_prime(num=1097):
    num = str(num)
    n = 1
    out = []
    while n < len(num):
        out_i = [num[:n], num[n:]]
        if (out_i[0][0] != '0') & (out_i[1][0] != '0'):
            if is_prime(out_i[0]) & is_prime(out_i[1]):
                out.append(out_i)
        n+=1
    return out

num = 0
def next_prime(start=3):
    global num
    while is_prime(start) is False:
        start+=2
    return prime

prime_list = {}
prime_list[2] = [2]
prime_list[3] = [3]

while 1:
    

        