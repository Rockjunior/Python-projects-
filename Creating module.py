# -*- coding: utf-8 -*-
"""
Created on Thu Mar 30 12:28:57 2023

@author: ROCKJUNIOR ROMAN
"""

#importing module
#creating your own module

def checkIfPrime (numberTocheck):
    for x in range(2,numberTocheck):
        if (numberTocheck%x == 0):
            return False
        return True
    
import prime
answer = prime.checkIfPrime(13)
print(answer)