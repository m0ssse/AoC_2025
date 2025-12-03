def find_highest_number(s, n, curr):
    if not n:
        return curr
    l = len(s)
    prefix = s[:l-n+1]
    d = max(prefix)
    i = s.find(d)
    curr = 10*curr+int(d)
    return find_highest_number(s[i+1:], n-1, curr)

def part1(fname):
    res = 0
    with open(fname) as file:
        for line in file:
            x = find_highest_number(line.strip(), 2, 0)
            res+=x
            
    return res

def part2(fname):
    res = 0
    with open(fname) as file:
        for line in file:
            x = find_highest_number(line.strip(), 12, 0)
            res+=x
    return res

if __name__=="__main__":
    fname = "input.txt"
    print(part1(fname))
    print(part2(fname))
    