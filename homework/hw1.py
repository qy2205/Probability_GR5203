# -*- coding: utf-8 -*-
"""
Created on Sun Sep  9 21:35:38 2018
@author: Quan Yuan
"""
import math
def combination(n, m):
    '''take m form n, order doesn't matter'''
    return math.factorial(n)/math.factorial(m)/(math.factorial(n-m))
def permutation(n, m):
    return math.factorial(n)/math.factorial(n-m)

print(combination(13, 5))