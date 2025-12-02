#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  1 16:23:53 2025

@author: ashleytokarzewski
"""
Answer = 0
Total = 50

def OverUnderFlow(w): 
    if w > 99:
        w = w - 100
        return OverUnderFlow(w)          
    elif w < 0:
        w = w + 100 
        return OverUnderFlow(w)
    else:
        return w

with open('data.txt', 'r') as file:
    Input = file.read().splitlines()
    for i in Input:
        if i.startswith("L"):
            Total -= int(i[1:])     
        else:
            Total += int(i[1:])
        if (OverUnderFlow(Total)) == 0:
            Answer += 1
print ("The Answer is:",Answer)
        
