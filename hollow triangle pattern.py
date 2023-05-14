# -*- coding: utf-8 -*-
"""
Created on Mon Mar 27 23:16:48 2023

@author: ROCKJUNIOR ROMAN
"""

#hollow triangle pattern

n=5
for i in range(1,n+1):
    for j in range(i):
        if j==0 or j==i-1:
            print('*',end='')
        else:
            if i!=n:
                print('',end='')
            else:
                print('*',end='')
    print()



