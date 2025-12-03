#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  1 16:23:53 2025

@author: ashleytokarzewski
"""
Answer = 0 
Input=[]
RangeArray = []
j=0
with open('input.txt', 'r') as file:
    Input = file.read()
    Input = Input.split(",")
    for k in range(0,len(Input)):
            ItemRange = Input[k].split("-")
            RangeArray = list(range(int(ItemRange[0]),int(ItemRange[1])))
            for i in RangeArray:
                Number= str(RangeArray[j])
                NumberLength= len(Number)
                if NumberLength % 2 == 0:
                    NumberLength = int(NumberLength/2)
                    if Number[:NumberLength] == Number[-NumberLength:]:
                        Answer += int(Number)
    
                if j == len(RangeArray) -1:
                    j = 0
                else:
                    j += 1
                      
print ("The Answer is:",Answer)
        

#For 1st digit of integer check against every other number in integar, if one
#is found to not match, if it doesnt group the first 2 together and test those
#continue until number your checking is half the length of the number. 