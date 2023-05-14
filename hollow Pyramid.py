# -*- coding: utf-8 -*-
"""
Created on Mon Mar 27 23:32:40 2023

@author: ROCKJUNIOR ROMAN
"""

#hollow Pyramid

n=10
for i in range(n):
    for j in range(n-i-1):
        print('',end='')
    for k in range(2*i+1):
        if k==0 or k==2*i:
           print('*',end='')
        else:
            if i==n-1:
                print('*',end='')
            else:
                print('',end='')
            
    print()