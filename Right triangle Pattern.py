# -*- coding: utf-8 -*-
"""
Created on Mon Mar 27 23:09:36 2023

@author: ROCKJUNIOR ROMAN
"""

#Right triangle pattern

n=5
for i in range(n):
    for j in range(1,n-1):
        print("",end="")
    for k in range(0,i+1):
        print("*",end="")
    print()