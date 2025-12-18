#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  8 12:55:25 2025

@author: ashleytokarzewski
"""

def cephalopod_total(filename):
    # Read lines and normalize to equal width
    with open(filename, 'r') as f:
        lines = [line.rstrip('\n') for line in f]

    width = max(len(line) for line in lines)
    lines = [line.ljust(width) for line in lines]

    rows = len(lines)
    lastrow = rows - 1

    sep_cols = [c for c in range(width) if all(lines[r][c] == ' ' for r in range(rows))]
    chunks = []
    current = []
    for c in range(width):
        if c in sep_cols:
            if current:
                chunks.append(current)
                current = []
        else:
            current.append(c)
    if current:
        chunks.append(current)

    total = 0
    for chunk in reversed(chunks):
        Operator = None
        for c in chunk:
            ch = lines[lastrow][c]
            if ch in '+*':
                Operator = ch
                break
        nums = []
        for c in reversed(chunk):
            digits = ''.join(lines[r][c] for r in range(rows - 1))   
            digits = ''.join(ch for ch in digits if ch != ' ')
            if digits:
                nums.append(int(digits))

        # Evaluate this problem
        if Operator == '+':
            value = sum(nums)
        elif Operator == '*':
            value = 1
            for n in nums:
                value *= n
        else:
            raise ValueError(f"Unknown operator {Operator}")

        total += value

    return total


if __name__ == "__main__":
    print(cephalopod_total("Input.txt"))
