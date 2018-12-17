# -*- coding: utf-8 -*-
"""
Created on Sun Oct  1 13:51:29 2017

@author: Jack
"""

import numpy as np

grid = np.loadtxt("grid.txt", dtype=int)

#==============================================================================
# print(np.prod(grid[0,16:16+4]))
#==============================================================================

def horizontal():
    """finds the largest horizontal string of numbers"""
    x = 0
    y = 0
    ans = 0
    while y < 20:
        while x < 17:
            ansint = np.prod(grid[y,x:x+4])
            if ansint > ans:
                ans = ansint
            x+=1
        x = 0
        y+=1
    return ans

def vertical():
    """finds the largest vertical product of numbers"""
    x = 0
    y = 0
    ans = 0
    while x < 20:
        while y < 17:
            ansint = np.prod(grid[y:y+4,x])
            if ansint > ans:
                ans = ansint
            y+=1
        y = 0
        x+=1
    return ans

def right_diag():
    """blah blah blah for diagonal leaning to the right"""
    x = 0
    y = 0
    ans = 0
    while y<17:
        while x<17:
            ansint = np.prod(np.diag(grid[y:y+4, x:x+4]))
            if ansint > ans:
                ans = ansint
            x+=1
        x = 0
        y+=1
    return ans

def left_diag():
    """blah blah blah for diagonal leaning to the left"""
    x = 0
    y = 0
    ans = 0
    while y<17:
        while x<17:
            ansint = np.prod(np.diag(np.flip(grid[y:y+4, x:x+4], 1)))
            if ansint > ans:
                ans = ansint
            x+=1
        x = 0
        y+=1
    return ans

v = vertical()
h = horizontal()
r = right_diag()
l = left_diag()

answers = np.array([v, h, r, l])

print(answers)
print(max(answers))