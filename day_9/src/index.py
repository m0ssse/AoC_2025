from itertools import combinations
import numpy as np
import matplotlib.pyplot as plt

def read_input(fname):
    with open(fname) as file:
        return [tuple([int(x) for x in line.split(",")]) for line in file]

def part1(points):
    max_area = 0
    for (x1, y1), (x2, y2) in combinations(points, 2):
        max_area = max(max_area, (abs(x1-x2)+1)*(abs(y1-y2)+1))
    return max_area

def visu(points):
    points.append(points[0])
    xs, ys = [], []
    for x, y in points:
        xs.append(x)
        ys.append(y)
    points.pop()
    plt.figure()
    plt.plot(xs, ys)
    plt.show()


if __name__=="__main__":
    fname = "input.txt"
    points = read_input(fname)
    print(part1(points))
    visu(points)