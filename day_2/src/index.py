def read_input(fname):
    ranges = []
    with open(fname) as file:
        contents = file.read().split(",")
    for range_str in contents:
        a, b = [int(x) for x in range_str.split("-")]
        ranges.append((a, b))
    return ranges

def part1(fname):
    ranges = read_input(fname)
    res = 0
    for x in range(1, 10**5):
        doubled = int(2*str(x))
        for a, b in ranges:
            if a<=doubled<=b:
                res+=doubled
                break
    return res

def part2(fname):
    ranges = read_input(fname)
    invalid = set()
    for x in range(1, 10**5):
        for n in range(2, 11):
            multiplied = int(n*str(x))
            for a, b in ranges:
                if a<=multiplied<=b:
                    invalid.add(multiplied)
    return sum(invalid)


if __name__=="__main__":
    fname = "input.txt"
    print(part1(fname))
    print(part2(fname))