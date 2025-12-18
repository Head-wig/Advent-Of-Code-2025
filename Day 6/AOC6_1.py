#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  8 11:41:05 2025

@author: ashleytokarzewski
"""
Input=[]
RangeList = []
Answer = 0
InRange = []
Fresh = 0 
MergedRanges = []
Row = []
Equations= [()]
j=0
with open('Test.txt', 'r') as file:
    Input = file.read().split("\n")
    for line in Input:
        Row = line.split()
        for i in Row:
            if len(Equations) <= j:
                Equations.append(())
            Equations[j] += (i,)
            j += 1
        j = 0
    for math in Equations:
        Solution = 0
        SigDig =len(max(math, key=len))
        for d in math:
            if isinstance(d, int):
                num = list(str(d))
                for j in range(0,SigDig):
                    if j > len(num) :
                        pass
                    else: 
                        Equations += (num[j])
                
            elif d == "*":
                if Solution == 0:
                    Solution = 1
                Solution = Solution*int(math[j])
            elif d == "+":
                Solution += math
               
                
            
# =============================================================================
#
#         Answer = Answer + Solution        
# print (Answer)
# =============================================================================
