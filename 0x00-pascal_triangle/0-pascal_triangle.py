#!/usr/bin/python3
"""
Pascal Triangle algoo
"""


def pascal_triangle(n):
    """Returning pascall list of ints representing pascall triangle"""
    if n <= 0:
        return []
    pascall = [[] for h in range(n)]
    for h in range(n):
        for j in range(h + 1):
            if j < h:
                if j == 0:
                    pascall[h].append(1)
                else:
                    pascall[h].append(pascall[h - 1][j] + pascall[h - 1][j - 1])
            elif j == h:
                pascall[h].append(1)
    return pascall
