"""
Pascal's triangle
"""

def pascal_triangle(n):
    """
        create a function that returns a list of lists of integers
        representing Pascal's triangle of n
    """
    res = []
    if n > 0:
        for i in range(1, n + 1):
            level = []
            C = 1
            for j in range(1, i + 1):
                level.append(C)
                C = C * (i - j) // j
            res.append(level)
    return res