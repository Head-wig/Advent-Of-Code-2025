#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  1 16:23:53 2025

@author: ashleytokarzewski
"""
Answer = 0
Input = []
RangeArray = []

def invalid(num: int) -> bool:
    s = str(num)
    L = len(s)
    for w in range(1, L // 2 + 1):
        if L % w != 0:
            continue
        pattern = s[:w]
        repeats = L // w
        if pattern * repeats == s:
            return True
    return False

with open('input.txt', 'r') as file:
    Input = file.read().strip().split(",")

    for k in range(0, len(Input)):
        if not Input[k]:
            continue
        ItemRange = Input[k].split("-")
        RangeArray = list(range(int(ItemRange[0]), int(ItemRange[1])+ 1))
        for num in RangeArray:
            if invalid(num):
                Answer += num

print("The Answer is:", Answer)

        

#For 1st digit of integer check against every other number in integar, if one
#is found to not match, if it doesnt group the first 2 together and test those
#continue until number your checking is half the length of the number. 