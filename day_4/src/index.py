def read_input(fname):
    with open(fname) as file:
        return [list(line.strip()) for line in file]
    
def part1(grid):
    to_remove = []
    n, m = len(grid), len(grid[0])
    for i, row in enumerate(grid):
        for j, c in enumerate(row):
            if c==".":
                continue
            neighb_count = 0
            for di in range(-1, 2):
                ii = i+di
                for dj in range(-1, 2):
                    if di==0 and dj==0:
                        continue
                    jj = j+dj
                    if ii<0 or ii>=n or jj<0 or jj>=m:
                        continue
                    if grid[ii][jj]=="@":
                        neighb_count+=1
            if neighb_count<4:
                to_remove.append((i, j))
    return to_remove

def part2(grid):
    res = 0
    to_remove = part1(grid)
    while to_remove:
        res+=len(to_remove)
        for i, j in to_remove:
            grid[i][j] = "."
        to_remove = part1(grid)
    return res

def part2_fast(grid):
    deltas = [
        (0, 1),
        (0, -1),
        (1, 1),
        (1, -1),
        (-1, 1),
        (-1, -1),
        (1, 0),
        (-1, 0)
    ]
    n, m = len(grid), len(grid[0])
    neighb_counts = [[0 for _ in range(m)] for _ in range(n)]
    for i, row in enumerate(grid):
        for j, _ in enumerate(row):
            for di, dj in deltas:
                ii, jj = i+di, j+dj
                if ii<0 or ii>=n or jj<0 or jj>=m:
                    continue
                if grid[ii][jj] == "@":
                    neighb_counts[i][j]+=1
    queue = []
    for i, row in enumerate(neighb_counts):
        for j, x in enumerate(row):
            if grid[i][j]=="@" and x<4:
                queue.append((i, j))
    visited = set()
    res1 = len(queue)
    k = 0
    while k<len(queue):
        i, j = queue[k]
        k+=1
        visited.add((i, j))
        grid[i][j] = "."
        for di, dj in deltas:
            ii, jj = i+di, j+dj
            if ii<0 or ii>=n or jj<0 or jj>=m:
                continue
            neighb_counts[ii][jj]-=1
            if neighb_counts[ii][jj]<4 and grid[ii][jj]=="@" and (ii, jj) not in visited:
                queue.append((ii, jj))
                visited.add((ii, jj))
    res2 = len(visited)
    return res1, res2

    


if __name__=="__main__":
    fname = "input.txt"
    print(part2_fast(read_input(fname)))
