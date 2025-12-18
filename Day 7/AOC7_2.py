#!/usr/bin/env python3
# -*- coding: utf-8 -*-

Answer = 0

with open('Input.txt', 'r') as file:
    Input = file.read().splitlines()

StartRow = 0
StartCol = 0
Found = False
for r, line in enumerate(Input):
    if "S" in line:
        StartRow = r
        StartCol = line.index("S")
        break

H = len(Input)
W = len(Input[0])

Active = {StartCol: 1}
Row = StartRow

while Active:
    if Row == H - 1:
        Answer += sum(Active.values())
        break

    NextRow = Row + 1
    NewActive = {}

    for col, count in Active.items():
        if col < 0 or col >= W:
            Answer += count
            continue

        ch = Input[NextRow][col]

        if ch == "." or ch == "S":
            NewActive[col] = NewActive.get(col, 0) + count

        elif ch == "^":
            left = col - 1
            right = col + 1

            if left < 0:
                Answer += count
            else:
                NewActive[left] = NewActive.get(left, 0) + count

            if right >= W:
                Answer += count
            else:
                NewActive[right] = NewActive.get(right, 0) + count

        else:
            Answer += count

    Active = NewActive
    Row = NextRow

print(Answer)
