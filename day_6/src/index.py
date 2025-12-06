def read_input(fname):
    rows = []
    with open(fname) as file:
        lines = file.readlines()
        widths = find_column_widths(lines)
    with open(fname) as file:
        for line in file:
            new_row = []
            i = 0
            for w in widths:
                new_row.append(line[i:i+w-1])
                i+=w
            rows.append(new_row)
    return rows

def find_column_widths(lines):
    widths = []
    w = 1
    for i in range(1, len(lines[-1])):
        if lines[-1][i] == " ":
            w+=1
        else:
            widths.append(w)
            w = 1
    widths.append(w+1)
    return widths

def group_blocks(lines):
    blocks = []
    for j in range(len(lines[0])):
        block = []
        for line in lines:
            block.append(line[j])
        blocks.append(block)
    return blocks

def evaluate(block):
    if "+" in block[-1]:
        res = 0
        for x in block[:-1]:
            res+=int(x)
    else:
        res = 1
        for x in block[:-1]:
            res*=int(x)
    
    return res

def transpose(block):
    transposed = []
    for j in range(len(block[0])):
        new_row = ""
        for i in range(len(block)):
            new_row+=block[i][j]
        transposed.append(new_row)
    return transposed

def get_sum(lines, j):
    res = 0
    for i in range(len(lines)-1):
        res+=int(lines[i][j])
    return res

def get_product(lines, j):
    res = 1
    for i in range(len(lines)-1):
        res*=int(lines[i][j])
    return res

def part1(blocks):
    return sum([evaluate(block) for block in blocks])

def part2(blocks):
    res = 0
    for block in blocks:
        transformed = transpose(block[:-1])
        transformed.append(block[-1])
        res+=evaluate(transformed)
    return res

fname = "input.txt"
lines = read_input(fname)
blocks = group_blocks(lines)
print(part1(blocks))
print(part2(blocks))
