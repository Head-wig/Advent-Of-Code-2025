#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 8 2025

@author: ashleytokarzewski
"""
Area = 0
LargestArea = 0
# Read input list of junction boxes
with open('Input.txt', 'r') as file:
    Input = file.read().strip("\n")
    points = []
    for line in Input.splitlines():
        x, y = line.split(',')
        points.append((int(x), int(y)))
    for pair in points:
        for testpair in points: 
            x1,y1 = pair
            x2, y2 = testpair
            Area = (abs((x2-x1))+1)*(abs((y2-y1 ))+1)
            if Area >= LargestArea:
                LargestArea = Area
    print ("The Answer is:",LargestArea)