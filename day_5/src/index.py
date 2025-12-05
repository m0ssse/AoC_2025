def read_input(fname):
    with open(fname) as file:
        fresh_ranges, ids = file.read().strip().split("\n\n")
        fresh_ranges = fresh_ranges.split()
        for i, row in enumerate(fresh_ranges):
            a, b = [int(x) for x in row.split("-")]
            fresh_ranges[i] = (a, b)
        ids = [int(x) for x in ids.split()]
        return fresh_ranges, ids
    
def part1(fname):
    ranges, ids = read_input(fname)
    res = 0
    for x in ids:
        for a, b in ranges:
            if a<=x<=b:
                res+=1
                break
    return res

def part2(fname):
    ranges, _ = read_input(fname)
    ranges.sort()
    merged = []
    curr_start, curr_end = ranges[0]
    for i in range(1, len(ranges)):
        a, b = ranges[i]
        if curr_start<=a<=curr_end+1:
            curr_end = max(curr_end, b)
        else:
            merged.append((curr_start, curr_end))
            curr_start, curr_end = a, b
    merged.append((curr_start, curr_end))
    res = 0
    for a, b in merged:
        res+=(b-a)+1
    return res


if __name__=="__main__":
    fname = "input.txt"
    print(part1(fname))
    print(part2(fname))