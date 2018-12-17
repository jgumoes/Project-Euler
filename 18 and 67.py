# -*- coding: utf-8 -*-
"""
Created on Fri Jun  8 14:53:07 2018

@author: Jack

Project Euler problems 18 and 67
"""

t0 = [[3], [7, 4], [2, 4, 6], [8, 5, 9, 3]]

t18 = ["75",
"95 64",
"17 47 82",
"18 35 87 10",
"20 04 82 47 65",
"19 01 23 75 03 34",
"88 02 77 73 07 63 67",
"99 65 04 28 06 16 70 92",
"41 41 26 56 83 40 80 70 33",
"41 48 72 33 47 32 37 16 94 29",
"53 71 44 65 25 43 91 52 97 51 14",
"70 11 33 28 77 73 17 78 39 68 17 57",
"91 71 52 38 17 14 91 43 58 50 27 29 48",
"63 66 04 68 89 53 67 30 73 16 69 87 40 31",
"04 62 98 27 23 09 70 98 73 93 38 53 60 04 23"]

for i in range(0, len(t18)):
    t18[i] = t18[i].split()
    for v in range(0, len(t18[i])):
        t18[i][v] = int(t18[i][v])

def find_path(t):
    paths = {0: t[-1]}
    for i in range(2, len(t)+1):
        K = paths[i-2]
        row = []
        for iv in range(0, len(t[-i])):
            if K[iv]>K[iv+1]:
                row.append(t[-i][iv]+K[iv])
            else:
                row.append(t[-i][iv]+K[iv+1])
        paths[i-1] = row
    return paths[len(t)-1]

def q67():
    with open("p067_triangle.txt") as f:
        t67 = f.read()
    t67 = t67.split("\n")[:-1]
    
    for i in range(0, len(t67)):
        t67[i] = t67[i].split()
        for v in range(0, len(t67[i])):
            t67[i][v] = int(t67[i][v])
    
    return find_path(t67)