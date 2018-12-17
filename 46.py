# -*- coding: utf-8 -*-
"""
Created on Sat Jan 28 16:47:03 2017

@author: Jack

project euler question 46
"""

import numpy as np

def is_prime(num):
    """Checks if number num is a prime number. 2, 3, and 5 won't be caught.
    num must be odd"""
    num = int(num)
    if num==1:
        return False
    if num==2:
        return True
    if num%2 == 0:
        return False
    l = np.linspace(3, num/2 +1, num/4, dtype=int)
    ans = num%l
    for i in ans:
        if i == 0:
            return False
    return True

def find_ans(up=10000):
    """Finds the answer to the question"""
    all_n = np.linspace(1, up, up, dtype=float)
    all_p = np.array([])
    all_c = np.array([])

    for i in all_n[1:]:
        if is_prime(i) == True:
            all_p = np.append(all_p, i)
        elif i%2 != 0:
            all_c = np.append(all_c, i)
    
    for number in all_c:
        found = False
        inte = np.sqrt((number - all_p)/2.)
        for val in inte:
            if np.isnan(val) == False:
                if val - int(val) == 0:
                    found = True
                    break
            # return "%d is first number" % (number)
        if found == True:
            print str(number) + "\t" + str(val)
        else:
            return "%d is first number" % (number)


