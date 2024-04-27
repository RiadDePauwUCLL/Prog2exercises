from itertools import pairwise

def total_distance(path, distance):
    xd = 0
    for x, y in pairwise(path):
        xd += distance(x, y)
    return xd