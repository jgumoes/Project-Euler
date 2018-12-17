# -*- coding: utf-8 -*-
"""
Created on Mon Jan 30 15:44:23 2017

@author: Jack

project euler question 571
https://projecteuler.net/problem=571
"""

def dec_to_bin(num):
    """converts a decimal number to a binary number"""
    c = 0
    ans = ""
    while num/(2**c) > 0:
        c += 1
    c -= 1
    while c >= 0:
        ans += str(num/(2**c))
        #print ans
        num = num%(2**c)
        c -= 1
    return ans

def dec_to_radix(num, base):
    """converts a decimal number to a number system of base base
    ie. if base = 2, convert decimal to binary"""
    c = 0
    ans = ""
    num = int(num)
    while num/(base**c) > 0:
        c += 1
    c -= 1
    while c >= 0:
        ans_int = num/(base**c)
        if ans_int == 10:
            ans_int = 'a'
        elif ans_int == 11:
            ans_int = 'b'
        ans += str(ans_int)
        #print ans
        num = num%(base**c)
        c -= 1
    return ans

def radix_to_dec(num, base):
    """converts a number of a number system to a decimal
    ie. if base is 2, converts number from decimal to binary"""
    num = str(num)
    c = len(num) - 1
    ans = 0
    while c >= 0:
        ans_int = num[len(num)-1 - c]
        if ans_int == 'a':
            ans_int = 10
        elif ans_int == 'b':
                ans_int = 11
        ans += int(ans_int) * (base**c)
        # print ans_int, c, ans
        c -= 1
    return ans

def is_pan(num, base):
    """checks if a number is a pandigital for it's base"""
    num = str(num)
    while 1:
        if num[0] == "0":
            num = num[1:]
        else:
            break
    char = "0123456789ab"
    c = 0
    while c < base:
        if char[c] not in num:
            return False
        c += 1
    while c < len(char):
        if char[c] in num:
            return False
        c += 1
    # print "%s is %d pandigital" % (num, base)
    return True

def is_sup_pan(num, base=10):
    """checks if a decimal number is a super-pandigital number up to base
    defaults to 10-super-pandigital number"""
    num = radix_to_dec(num, base)
    while base >= 2:
        if is_pan(dec_to_radix(num, base), base) is False:
        #if is_pan(num, base) is False:
            #print num, base
            return False
        #else:
        #    print base, True
        base -= 1
    return True

def to_num(num):
    """quick and easy way to turn a string digit to a number"""
    if num == "a":
        return 10
    elif num =="b":
        return 11
    else:
        return int(num)

def to_str(num):
    """quick and easy way to turn a digit into a string"""
    if num == 10:
        return 'a'
    elif num == 11:
        return 'b'
    else:
        return str(num)
    

def find_next_pan(num=1624598730, base=10):
    """quick way to find pandigital numbers. test answer is 1624703589"""
    num = str(num)[::-1]
    b = '0123456789ab'[:base]
    c = 1
    missing = ""
    while c <= base:
        if to_num(num[c]) < to_num(num[c-1]):
            staying = num[c+1:][::-1]
            n = to_num(num[c])
            #print n, c, staying
            break
        c+=1
    while 1:
        n +=1
        if to_str(n) not in staying:
            staying+=to_str(n)
            break
    for i in b:
        if i not in staying:
            missing += i
    return staying + missing

def quick_find_pan():
    ans = []
    num = str(1023456789)
    #num = 1624573890
    while len(ans) <= 10000:
        num = find_next_pan(num)
        ans.append(num)
    return ans

def quick_find_10_sup_pan():
    ans = []
    num = str(1023456789)
    while len(ans) < 10:
        if is_sup_pan(num, 10) is True:
            ans.append(num)
            print num
        num = find_next_pan(num)
    
    ans_out = 0
    for i in ans:
        ans_out += int(i)
    return ans, ans_out

num_check = 0

def quick_find_12_sup_pan():
    ans = ["217904b5a638", "2307185a64b9", "36752b80419a", "394017b8526a", "395b41267a80"]
    #number = "1023456789ab"
    #number = "251809b47a36"
    #number = "2519370a4b68"
    number = "3a971b062458"
    count = 0
    while len(ans) < 10:
        if is_sup_pan(number, 12) is True:
            ans.append(number)
            print number
            
        #if count == 1000000:
        #    print "count cycled on " + str(number)
        #    count = 0
        #count += 1
        
        number = find_next_pan(number, 12)
        global num_check
        num_check = number
    
    ans_out = 0
    print ans
    for i in ans:
        ans_out += radix_to_dec(i, 12)
    return ans_out

#==============================================================================
# def find_pan():
#     """Finds pandigital numbers"""
#     ans = []
#     num = 1023456789
#     #num = 1624573890
#     while len(ans) <= 10000:
#     #while num < 1802964790:
#         if is_pan(num, 10) is True:
#             ans.append(num)
#             #if num-pre > 30000:
#             #    print pre, num
#             #pre = num
#         num += 1
#     #return ans, sum(ans)
#     print ans[-1]
#     return int(ans[-1])-int(ans[0])
# 
# def find_sup_pan():
#     """Finds super-pandigital number"""
#     #ans = []
#     ans = [1093265784, 1367508924, 1432598706, 1624573890, 1802964753]
#     #num = 1023456789
#     num = 2002964753
#     c = 0
#     while len(ans) <= 10:
#         if is_pan(num, 10) is True:
#             if is_sup_pan(num, 10) is True:
#                 ans.append(num)
#                 print num
#         num += 1
#         if c >= 100000000:
#             #print "current number is: " + str(num)
#             print ans
#             c = 0
#         c += 1
#     return ans, sum(ans)
#     
# def find_next_pan(num, base):
#     """quick way to find pandigital numbers"""
#     num = str(num)
#     b = '0123456789ab'[:base]
#     missing = []
#     excess = []
#     for i in b:
#         if num.count(i) == 0:
#             missing.append(i)
#         elif num.count(i) > 1:
#             excess.append(i)
#==============================================================================


    