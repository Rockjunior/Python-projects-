# -*- coding: utf-8 -*-
"""
Created on Mon Mar 27 23:28:51 2023

@author: ROCKJUNIOR ROMAN
"""

#Pyramid

n=10
for i in range(n):
    for j in range(n-i-1):
        print('',end='')
    for k in range(2*i+1):
        print('*',end='')
    print()