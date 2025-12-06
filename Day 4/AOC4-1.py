#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 4 2025

@author: ashleytokarzewski
"""

Answer = 0

with open('Input.txt', 'r') as file:
    Input = file.read()

Input = [list(line) for line in Input.splitlines()]
rows = len(Input)
col = len(Input[0])

dirs = [
    (-1, -1), (-1, 0), (-1, 1),
    (0, -1),           (0, 1),
    (1, -1), (1, 0),   (1, 1),
]

marked = [row[:] for row in Input]
accessible_count = 0

for i in range(rows):
    for j in range(col):
        if Input[i][j] != '@':
            continue

        NextTo = 0
        for k, m in dirs:
            n, l = i + k, j + m
            if 0 <= n < rows and 0 <= l < col:
                if Input[n][l] == '@':
                    NextTo += 1

        if NextTo < 4:
            accessible_count += 1
            marked[i][j] = 'x'

print("Accessible rolls:", accessible_count)
