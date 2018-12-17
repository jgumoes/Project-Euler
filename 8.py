# -*- coding: utf-8 -*-
"""
Created on Sun Jan 29 17:34:14 2017

@author: Jack

project euler question 8
"""

import numpy as np

numbers = np.array([])

for i in "73167176531330624919225119674426574742355349194934":
    numbers = np.append(numbers, int(i))
for i in "96983520312774506326239578318016984801869478851843":
    numbers = np.append(numbers, int(i))
for i in "85861560789112949495459501737958331952853208805511":
    numbers = np.append(numbers, int(i))
for i in "12540698747158523863050715693290963295227443043557":
    numbers = np.append(numbers, int(i))
for i in "66896648950445244523161731856403098711121722383113":
    numbers = np.append(numbers, int(i))
for i in "62229893423380308135336276614282806444486645238749":
    numbers = np.append(numbers, int(i))
for i in "30358907296290491560440772390713810515859307960866":
    numbers = np.append(numbers, int(i))
for i in "70172427121883998797908792274921901699720888093776":
    numbers = np.append(numbers, int(i))
for i in "65727333001053367881220235421809751254540594752243":
    numbers = np.append(numbers, int(i))
for i in "52584907711670556013604839586446706324415722155397":
    numbers = np.append(numbers, int(i))
for i in "53697817977846174064955149290862569321978468622482":
    numbers = np.append(numbers, int(i))
for i in "83972241375657056057490261407972968652414535100474":
    numbers = np.append(numbers, int(i))
for i in "82166370484403199890008895243450658541227588666881":
    numbers = np.append(numbers, int(i))
for i in "16427171479924442928230863465674813919123162824586":
    numbers = np.append(numbers, int(i))
for i in "17866458359124566529476545682848912883142607690042":
    numbers = np.append(numbers, int(i))
for i in "24219022671055626321111109370544217506941658960408":
    numbers = np.append(numbers, int(i))
for i in "07198403850962455444362981230987879927244284909188":
    numbers = np.append(numbers, int(i))
for i in "84580156166097919133875499200524063689912560717606":
    numbers = np.append(numbers, int(i))
for i in "05886116467109405077541002256983155200055935729725":
    numbers = np.append(numbers, int(i))
for i in "71636269561882670428252483600823257530420752963450":
    numbers = np.append(numbers, int(i))

length = len(numbers)
count = 0
answers = np.array([])
window = 13

while count < len(numbers) - 1 - window:
    answers = np.append(answers, np.prod(numbers[count:count+window]))
    count +=1

print np.max(answers)
