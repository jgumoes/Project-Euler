# -*- coding: utf-8 -*-
"""
Created on Tue Jan 24 13:11:46 2017

@author: Jack

question 4 of project euler
"""

def is_palindrome(number):
    """Is number a palindrome? I don't know; let's find out!"""
    num = str(number)
    c = 0
    l = len(num)
    while c < l/2:
        if num[c] == num[l-1-c]:
            c+=1
        else:
            return False
    return True

def find_palindrome(start):
    """Finds a palindrome by counting backwards from start"""
    while 1:
        #  print start
        if is_palindrome(start) is True:
            return start
        else:
            start -= 1

def find_factors(number):
    """finds the 3 digit factors of numer. If there aren't any, returns False"""
    c = 999
    while c > 99:
        #  print "\t" + str(c)
        if number/c < 1000:
            if number%c == 0:
                return c
            else:
                c -= 1
        else:
            return False
    return False

def q4():
    """solves question 4"""
    start = 999*999
    while 1:
        start = find_palindrome(start)
        f = find_factors(start)
        if f is False:
            start -= 1
        else:
            return start, f, start/f


        