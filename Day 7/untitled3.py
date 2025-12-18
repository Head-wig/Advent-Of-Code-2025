#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 8 2025

@author: ashleytokarzewski
"""

Answer = 0

with open('Input.txt', 'r') as file:
    Input = file.read().splitlines()

    # Find S
    StartRow = 0
    StartCol = 0
    for r, line in enumerate(Input):
        if "S" in line:
            StartRow = r
            StartCol = line.index("S")
            break
    Active = [StartCol]
    SplittersHit = []
    Row = StartRow
    while Row < len(Input) - 1 and Active:
        NextRow = Row + 1
        NextLine = Input[NextRow]
        NewActive = []
        for col in Active:
            if col < 0 or col >= len(NextLine):
                continue
            ch = NextLine[col]
            if ch == "." or ch == "S":
                if col not in NewActive:
                    NewActive.append(col)
            elif ch == "^":
                pos = (NextRow, col)
                if pos not in SplittersHit:
                    SplittersHit.append(pos)
                    Answer += 1  
                if col - 1 >= 0 and (col - 1) not in NewActive:
                    NewActive.append(col - 1)
                if col + 1 < len(NextLine) and (col + 1) not in NewActive:
                    NewActive.append(col + 1)
            else:
                pass

        Active = NewActive
        Row = NextRow

    print( Answer)
