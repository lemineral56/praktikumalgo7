#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 10 23:14:32 2022

@author: rhenatabella
"""

def is_prima ():
    x=int(input("Masukan angkanya: "))
    for i in range(2, x):
        if x % i == 0:
            return False
    return True
        
p=is_prima()
print(p)
