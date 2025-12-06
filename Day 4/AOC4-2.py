#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 4 2025

@author: ashleytokarzewski
"""

# Read input grid
with open('Input.txt', 'r') as file:
    Input = file.read().strip("\n")

grid_original = [list(line) for line in Input.splitlines()]
rows = len(grid_original)
cols = len(grid_original[0])
grid = [row[:] for row in grid_original]
removed = 0

neighbor_dirs = [
    (-1, -1), (-1, 0), (-1, 1),
    (0, -1),           (0, 1),
    (1, -1),  (1, 0),  (1, 1),
]



while True:
    Out = []

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] != '@':
                continue

            neighbor_at = 0
            for di, dj in neighbor_dirs:
                ni, nj = i + di, j + dj
                if 0 <= ni < rows and 0 <= nj < cols:
                    if grid[ni][nj] == '@':
                        neighbor_at += 1

            if neighbor_at < 4:
                Out.append((i, j))

    if not Out:
        break
    
    for i, j in Out:
        grid[i][j] = '.'   

    removed += len(Out)

print("Total rolls that can be removed:", removed)
