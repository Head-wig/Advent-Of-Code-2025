#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 8 2025

@author: ashleytokarzewski
"""

# Read input list of junction boxes
with open('Input.txt', 'r') as file:
    Input = file.read().strip("\n")

points = []
for line in Input.splitlines():
    x, y, z = line.split(',')
    points.append((int(x), int(y), int(z)))

n = len(points)

# Build all edges (squared distance to avoid sqrt)
edges = []
for i in range(n):
    x1, y1, z1 = points[i]
    for j in range(i + 1, n):
        x2, y2, z2 = points[j]

        dx = x1 - x2
        dy = y1 - y2
        dz = z1 - z2

        dist2 = dx*dx + dy*dy + dz*dz
        edges.append((dist2, i, j))

# Sort edges by distance (ascending)
edges.sort(key=lambda e: e[0])

# ---- Union-Find (Disjoint Set Union) ----
parent = list(range(n))
size = [1] * n

def find(x):
    while parent[x] != x:
        parent[x] = parent[parent[x]]
        x = parent[x]
    return x

def union(a, b):
    ra = find(a)
    rb = find(b)

    if ra == rb:
        return False

    # attach smaller tree under larger
    if size[ra] < size[rb]:
        ra, rb = rb, ra

    parent[rb] = ra
    size[ra] += size[rb]
    return True

# ---- Keep connecting until everything is in one circuit ----
components = n
last_i = None
last_j = None

for dist2, i, j in edges:
    merged = union(i, j)
    if merged:
        components -= 1
        last_i = i
        last_j = j
        if components == 1:
            break

# Get the X coordinates of the last two connected junction boxes
x1 = points[last_i][0]
x2 = points[last_j][0]

answer = x1 * x2

print(answer)
