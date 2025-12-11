def read_input(fname):
    graph = {}
    with open(fname) as file:
        for line in file:
            line = line.strip()
            parent, children = line.split(": ")
            graph[parent] = children.split()
    return graph

def part1(graph):
    ways = {"out": 1}
    blacklist = set()
    count_paths_from(graph, "you", ways, blacklist)
    return ways["you"]

def part2(graph):
    #count ways from srv to fft that don't visit dac or out
    ways = {"fft": 1}
    blacklist = set(["out", "dac"])
    count_paths_from(graph, "svr", ways, blacklist)
    svr_to_fft = ways["svr"]
    #count ways from src to dac that don't visit fft or out
    ways = {"dac": 1}
    blacklist = set(["out", "fft"])
    count_paths_from(graph, "svr", ways, blacklist)
    svr_to_dac = ways["svr"]
    #count ways from dac to fft that don't visit out
    ways = {"fft": 1}
    blacklist = set(["out"])
    count_paths_from(graph, "dac", ways, blacklist)
    dac_to_fft = ways["dac"]
    #count ways from fft to dac that don't visit out
    ways = {"dac": 1}
    count_paths_from(graph, "fft", ways, blacklist)
    fft_to_dac = ways["fft"]
    #count ways from fft to out that don't visit dac
    ways = {"out": 1}
    blacklist = set(["dac"])
    count_paths_from(graph, "fft", ways, blacklist)
    fft_to_out = ways["fft"]
    #count ways from dac to out that don't visit fft
    ways = {"out": 1}
    blacklist = set(["fft"])
    count_paths_from(graph, "dac", ways, blacklist)
    dac_to_out = ways["dac"]
    res = svr_to_dac*dac_to_fft*fft_to_out+svr_to_fft*fft_to_dac*dac_to_out
    return res

def count_paths_from(graph, node, ways, blacklist):
    if node in ways:
        return ways[node]
    ways[node] = 0
    for next_node in graph[node]:
        if next_node in blacklist:
            continue
        ways[node]+=count_paths_from(graph, next_node, ways, blacklist)
    return ways[node]

if __name__=="__main__":
    fname = "input.txt"
    graph = read_input(fname)
    print(part1(graph))
    print(part2(graph))