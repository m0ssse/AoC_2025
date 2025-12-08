from itertools import combinations
from math import sqrt

class UnionFind:
    def __init__(self, nodes):
        self.n = len(nodes)
        self.parent = {x: x for x in nodes}
        self.component_size = {x: 1 for x in nodes}
        self.components = self.n

    def repres(self, x):
        while x!=self.parent[x]:
            x = self.parent[x]
        return x
    
    def merge(self, a, b):
        a = self.repres(a)
        b = self.repres(b)
        if a==b:
            return
        if self.component_size[a]<self.component_size[b]:
            a, b = b, a
        self.parent[b] = a
        self.component_size[a]+=self.component_size[b]
        self.components-=1

def read_input(fname):
    nodes = set()
    with open(fname) as file:
        for line in file:
            x, y, z = [int(a) for a in line.split(",")]
            nodes.add((x, y, z))
    return nodes

def distance(p1, p2):
    d = 0
    for a, b in zip(p1, p2):
        d+=(a-b)**2
    return sqrt(d)

def part1(nodes, N):
    uf = UnionFind(nodes)
    edges = []
    for p1, p2 in combinations(nodes, 2):
        edges.append((distance(p1, p2), p1, p2))
    edges.sort()
    i = 0
    while uf.components>1:
        _, p1, p2 = edges[i]
        i+=1
        uf.merge(p1, p2)
        if i==N:
            ans1 = sorted([uf.component_size[x] for x in nodes if uf.repres(x)==x], reverse=True)
    return ans1[0]*ans1[1]*ans1[2], p1[0]*p2[0]

if __name__=="__main__":
    #fname, N = "test.txt", 10
    fname, N = "input.txt", 1000
    nodes = read_input(fname)
    print(part1(nodes, N))
    