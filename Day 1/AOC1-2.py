#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  1 16:23:53 2025

@author: ashleytokarzewski
"""
Answer = 0      
Total = 50     

with open('data.txt', 'r') as file:
    Input = file.read().splitlines()
    for i in Input:
        Turn = int(i[1:])  
        if i.startswith("L"):
            Click = -1
        else:
            Click = 1
        for j in range(Turn):
            Total = (Total + Click) % 100  
            if Total == 0:                 #
                Answer += 1

print("The Answer is:", Answer)
