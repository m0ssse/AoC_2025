def part1(fname, pos=50):
    res = 0
    with open(fname) as file:
        for line in file:
            n = int(line[1:])
            if line[0]=="L":
                pos = (pos-n)%100
            else:
                pos = (pos+n)%100
            res+=pos==0
    return res

def part2(fname, pos=50):
    res = 0
    with open(fname) as file:
        for line in file:
            n = int(line[1:])
            d = 1 if line[0]=="R" else -1
            for _ in range(n):
                pos = (pos+d)%100
                res+=pos==0
    return res


if __name__=="__main__":
    fname = "input.txt"
    print(part1(fname))
    print(part2(fname))