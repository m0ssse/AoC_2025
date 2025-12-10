def read_input(fname):
    target_states = []
    buttons = []
    joltages = []
    with open(fname) as file:
        for line in file:
            line = line.strip()
            i1 = line.find("]")
            i2 = line.find("{")
            target_states.append(target_to_num(line[1:i1]))
            joltages.append(tuple([int(x) for x in line[i2+1:-1].split(",")]))
            wirings = line[i1+2:i2-1].split()
            wirings_on_line = []
            for w in wirings:
                buttons_for_w = tuple(int(x) for x in w[1:-1].split(","))
                wirings_on_line.append(wiring_to_num(buttons_for_w))
            buttons.append(wirings_on_line)
    return target_states, buttons, joltages

def target_to_num(s):
    res = 0
    for i, c in enumerate(s):
        if c=="#":
            res+=1<<i
    return res

def wiring_to_num(w):
    res = 0
    for x in w:
        res+=1<<x
    return res
    
def part1(targets, buttons):
    res = 0
    for t, b in zip(targets, buttons):
        res+=solve1(t, b)
    return res

def solve1(target, buttons):
    queue = [(0, 0)]
    visited = set()
    i = 0
    while i<len(queue):
        steps, state = queue[i]
        i+=1
        visited.add(state)
        if state == target:
            return steps
        for b in buttons:
            new_state = state^b
            if new_state in visited:
                continue
            visited.add(new_state)
            queue.append((steps+1, new_state))

if __name__=="__main__":
    fname = "input.txt"
    targets, buttons, joltages = read_input(fname)
    print(part1(targets, buttons))