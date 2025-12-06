#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  5 14:47:09 2025

@author: ashleytokarzewski
"""
Input=[]
RangeList = []
Answer = 0
InRange = []
with open('Input.txt', 'r') as file:
    Input = file.read().split("\n\n")
    Ranges = Input[0].split("\n")
    Items = Input[1].split("\n")
    for i in Ranges:
       irange = i.split("-")
       Start, End = int(irange[0]),int(irange[1])
       for k in Items:
           #print (k)
           if Start <= int(k) <= End and k not in InRange :
               print (k)
               InRange.append(k)
               #print (Start, End)
Answer = len(InRange)
print (Answer)

    

       
       