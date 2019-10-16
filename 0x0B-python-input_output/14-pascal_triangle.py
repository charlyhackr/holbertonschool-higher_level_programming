#!/usr/bin/python3

def pascal_triangle(n):
    """Represent Pascal Triangle of size n"""

    if n <= 0:
        return []

    triangles = [[1]]
    while len(triangles) != n:
        tria = triangles[-1]
        temp = [1]
        for m in range(len(tria) - 1):
            temp.append(tria[m] + tria[m + 1])
        temp.append(1)
        triangles.append(temp)
    return triangles
