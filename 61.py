# -*- coding: utf-8 -*-
"""
Created on Sun Oct  1 18:23:30 2017

@author: Jack
"""

import numpy as np

tri = np.array([], dtype=int)
sq = np.array([], dtype=int)
pent = np.array([], dtype=int)
hexa = np.array([], dtype=int)
hept = np.array([], dtype=int)
octa = np.array([], dtype=int)

trin = np.array([], dtype=int)
sqn = np.array([], dtype=int)
pentn = np.array([], dtype=int)
hexan = np.array([], dtype=int)
heptn = np.array([], dtype=int)
octan = np.array([], dtype=int)

n = 1
while 1:
    num = int(n*(n+1)/2)
    if num > 9999:
        break
    if num >= 1000:
        tri = np.append(tri, num)
        trin = np.append(trin, n)
    n+=1
#%%
n=1
while 1:
    num = int(n**2)
    if num > 9999:
        break
    if num >= 1000:
        sq = np.append(sq, num)
        sqn = np.append(sqn, n)
    n+=1

n=1
while 1:
    num = int(n*(3*n-1)/2)
    if num > 9999:
        break
    if num >= 1000:
        pent = np.append(pent, num)
        pentn = np.append(pentn, n)
    n+=1

n=1
while 1:
    num = int(n*(2*n-1))
    if num > 9999:
        break
    if num >= 1000:
        hexa = np.append(hexa, num)
        hexan = np.append(hexan, n)
    n+=1

n=1
while 1:
    num = int(n*(5*n-3)/2)
    if num > 9999:
        break
    if num >= 1000:
        hept = np.append(hept, num)
        heptn = np.append(heptn, n)
    n+=1

n=1
while 1:
    num = int(n*(3*n-2))
    if num > 9999:
        break
    if num >= 1000:
        octa = np.append(octa, num)
        octan = np.append(octan, n)
    n+=1
#%%

