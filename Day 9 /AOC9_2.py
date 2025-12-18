#!/usr/bin/env python3
import sys
from collections import defaultdict

def read_points_from_file(filename):
    pts = []
    with open(filename, "r") as file:
        for line in file:
            line = line.strip()
            if not line:
                continue
            x, y = map(int, line.split(","))
            pts.append((x, y))
    return pts

def build_polygon_edges(points):
    edges = []
    n = len(points)
    for i in range(n):
        x1, y1 = points[i]
        x2, y2 = points[(i + 1) % n]
        # All edges are axis-aligned per problem description
        if x1 != x2 and y1 != y2:
            raise ValueError("Input adjacency is not axis-aligned.")
        edges.append(((x1, y1), (x2, y2)))
    return edges

def compress_coords(points):
    xs = sorted({x for x, _ in points})
    ys = sorted({y for _, y in points})
    return xs, ys, {x:i for i,x in enumerate(xs)}, {y:i for i,y in enumerate(ys)}

def build_inside_grid(edges, xs, ys):
    W = len(xs) - 1
    H = len(ys) - 1
    inside = [[False]*W for _ in range(H)]

    # Collect only vertical edges
    vertical = []
    for (x1,y1),(x2,y2) in edges:
        if x1 == x2:
            ylo, yhi = sorted((y1,y2))
            if ylo != yhi:
                vertical.append((x1,ylo,yhi))

    for j in range(H):
        ymid = (ys[j] + ys[j+1]) * 0.5
        xs_int = []
        for x,ylo,yhi in vertical:
            if ylo <= ymid < yhi:
                xs_int.append(x)
        xs_int.sort()

        for i in range(W):
            xmid = (xs[i] + xs[i+1]) * 0.5
            # Count intersections to the left
            cnt = 0
            for xi in xs_int:
                if xi > xmid:
                    break
                cnt += 1
            inside[j][i] = (cnt % 2 == 1)

    return inside

def build_prefix(inside, xs, ys):
    H = len(inside)
    W = len(inside[0])
    prefix = [[0]*(W+1) for _ in range(H+1)]

    for j in range(H):
        dy = ys[j+1] - ys[j]
        rowsum = 0
        for i in range(W):
            if inside[j][i]:
                dx = xs[i+1] - xs[i]
                rowsum += dx*dy
            prefix[j+1][i+1] = prefix[j][i+1] + rowsum
    return prefix

def rect_area(prefix, xs, ys, xidx, yidx, x1, y1, x2, y2):
    ix1, ix2 = xidx[x1], xidx[x2]
    iy1, iy2 = yidx[y1], yidx[y2]

    inside_area = (
        prefix[iy2][ix2]
        - prefix[iy1][ix2]
        - prefix[iy2][ix1]
        + prefix[iy1][ix1]
    )

    rect_cont = (x2 - x1) * (y2 - y1)
    return inside_area == rect_cont

def main():
    points = read_points_from_file("Input.txt")
    if len(points) < 2:
        print(0)
        return

    edges = build_polygon_edges(points)
    xs, ys, xidx, yidx = compress_coords(points)
    inside = build_inside_grid(edges, xs, ys)
    prefix = build_prefix(inside, xs, ys)

    best = 0
    n = len(points)

    for i in range(n):
        x1, y1 = points[i]
        for j in range(i+1, n):
            x2, y2 = points[j]

            if x1 == x2 or y1 == y2:
                continue  # zero area

            xx1, xx2 = sorted((x1, x2))
            yy1, yy2 = sorted((y1, y2))

            # Must be aligned to compressed coordinate boundaries
            if xx1 not in xidx or xx2 not in xidx:
                continue
            if yy1 not in yidx or yy2 not in yidx:
                continue

            if rect_area(prefix, xs, ys, xidx, yidx, xx1, yy1, xx2, yy2):
                w = abs(x2 - x1) + 1
                h = abs(y2 - y1) + 1
                area_tiles = w * h
                if area_tiles > best:
                    best = area_tiles

    print(best)

if __name__ == "__main__":
    main()
