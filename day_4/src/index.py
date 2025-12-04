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


if __name__=="__main__":
    fname = "input.txt"
    print(len(part1(read_input(fname))))
    print(part2(read_input(fname)))
