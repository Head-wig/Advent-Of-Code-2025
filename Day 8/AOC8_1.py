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
    edges.sort(key=lambda e: e[0])
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
        if size[ra] < size[rb]:
            ra, rb = rb, ra
        parent[rb] = ra
        size[ra] += size[rb]
        return True
    connections = 0
    K = 1000
    for dist2, i, j in edges:
        if connections >= K:
            break
        union(i, j)
        connections += 1
    circuit_sizes = []
    seen = set()
    for i in range(n):
        r = find(i)
        if r not in seen:
            seen.add(r)
            circuit_sizes.append(size[r])
    circuit_sizes.sort(reverse=True)
    while len(circuit_sizes) < 3:
        circuit_sizes.append(1)
    a, b, c = circuit_sizes[:3]
    answer = a * b * c
    print(answer)
