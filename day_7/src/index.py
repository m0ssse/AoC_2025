def read_input(fname):
    with open(fname) as file:
        return [line.strip() for line in file]
    
def make_graph(grid):
    neighbs = {}
    for i, row in enumerate(grid):
        for j, c in enumerate(row):
            if c=="S":
                neighbs[(i, j)] = [find_next_splitter(grid, i, j)]
            elif c=="^":
                neighbs[(i, j)] = []
                next1 = find_next_splitter(grid, i, j+1)
                if next1:
                    neighbs[(i, j)].append(next1)
                next2 = find_next_splitter(grid, i, j-1)
                if next2:
                    neighbs[(i, j)].append(next2)
    return neighbs

def invert_graph(graph):
    inverted = {}
    for i, j in graph:
        for ii, jj in graph[(i, j)]:
            if (ii, jj) not in inverted:
                inverted[(ii, jj)] = []
            inverted[(ii, jj)].append((i, j))
    return inverted

def find_next_splitter(grid, i, j):
    n = len(grid)
    for ii in range(i, n):
        if grid[ii][j]=="^":
            return (ii, j)
    return (n, j)

def part1(grid):
    graph = make_graph(grid)
    #print(graph)
    n = len(grid)
    visited = set()
    for j, c in enumerate(grid[0]):
        if c=="S":
            dfs(graph, (0, j), visited, n)
    return len(visited)

def dfs(graph, node, visited, n):
    if node[0]==n:
        return
    visited.add(node)
    for next_node in graph[node]:
        if next_node in visited:
            continue
        dfs(graph, next_node, visited, n)

def part2(grid):
    graph = make_graph(grid)
    n, m = len(grid), len(grid[0])
    inverted = invert_graph(graph)
    ways = {}
    for i, row in enumerate(grid):
        for j, c in enumerate(row):
            if c == "S":
                ways[(i, j)] = 1
            elif c == "^":
                ways[(i, j)] = 0
                if (i, j) not in inverted:
                    continue
                for ii, jj in inverted[(i, j)]:
                    ways[(i, j)]+=ways[(ii, jj)]
    total = 0
    for j in range(m):
        if (n, j) in inverted:
            for ii, jj in inverted[(n, j)]:
                total+=ways[(ii, jj)]
    return total

if __name__=="__main__":
    fname = "input.txt"
    grid = read_input(fname)
    print(part1(grid)-1) #starting node is counted as visited but a split does not occur there
    print(part2(grid))