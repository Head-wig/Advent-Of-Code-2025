#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 5 14:47:09 2025

@author: ashleytokarzewski
"""
Input=[]
RangeList = []
Answer = 0
InRange = []
Fresh = 0 
MergedRanges = []
with open('Input.txt', 'r') as file:
    Input = file.read().split("\n\n")
    RangesRaw = Input[0].split("\n")
    Items = Input[1].split("\n")
    for i in RangesRaw:
       irange = i.split("-")
       Tuple = int(irange[0]),int(irange[1])
       RangeList.append(Tuple)
       RangeList.sort()
    for start, end in RangeList:
        if not MergedRanges:
            MergedRanges.append([start, end])
        else:
            last_start, last_end = MergedRanges[-1]
            if start <= last_end + 1:
                MergedRanges[-1][1] = max(last_end, end)
            else:
                MergedRanges.append([start, end])
total = sum(end - start + 1 for start, end in MergedRanges)

print (total)
    

       
       