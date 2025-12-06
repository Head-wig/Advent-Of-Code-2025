#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  3 13:36:38 2025

@author: ashleytokarzewski"""

Answer = 0 

with open('Input.txt', 'r') as file:
    Input = file.read().split("\n")
    for i in Input:
        AnsHold =0 
        for j in range(0,len(i)):
            for k in range(j+1,len(i)):
             test = int(i[j]) * 10 + int(i[k])
             if test > AnsHold:
                 AnsHold = test
        Answer += AnsHold
print ("The Answer is:",Answer)
        
