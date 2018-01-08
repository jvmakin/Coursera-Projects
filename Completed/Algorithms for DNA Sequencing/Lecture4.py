""" PRACTICAL: Implementing SCS """
import itertools

# From previous lecture
def overlap(a, b, min_length=3):
    start = 0
    while True:
        start = a.find(b[:min_length], start)
        if start == -1:
            # no overlap
            return 0
        if b.startswith(a[start:]):
            return len(a)-start
        else:
            start += 1

# Shortest common substring of strings ss
def scs(ss):
    shortest_sup = None
    for ssperm in itertools.permutations(ss):
        sup = ssperm[0]
        for i in range(len(ss)-1):
            olen = overlap(ssperm[i], ssperm[i+1], min_length=1)
            sup += ssperm[i+1][olen:]
        if shortest_sup is None or len(sup) < len(shortest_sup):
            shortest_sup = sup
    return shortest_sup

# print scs(['ACGGATGAGC', 'GAGCGGA', 'GAGCGAG'])

""" PRACTICAL: Implementing greedy SCS """

# Helper function - picks max overlaps
def pick_maximal_overlap(reads, k):
    reada, readb = None, None
    best_olen = 0
    for a,b in itertools.permutations(reads, 2):
        olen = overlap(a, b, min_length = k)
        if olen > best_olen:
            reada, readb = a, b
            best_olen = olen
    return reada, readb, best_olen

# Greedy SCS
def greedy_scs(reads, k):
    read_a, read_b, olen = pick_maximal_overlap(reads, k)
    while olen > 0:
        reads.remove(read_a)
        reads.remove(read_b)
        reads.append(read_a + read_b[olen:])
        read_a, read_b, olen = pick_maximal_overlap(reads, k)
    return ''.join(reads)

# print greedy_scs(['ABC', 'BCA', 'CAB'], 2)

# print greedy_scs(['ABCD', 'CDBC', 'BCDA'], 1)

""" PRACTICAL: De Bruijn Graphs/Eulerian Walks """

# Makes a debruijn graph
def de_bruijn_ize(st, k):
    edges = []
    nodes = set()
    for i in range(len(st) - k + 1):
        edges.append((st[i:i+k-1], st[i+1:i+k]))
        nodes.add(st[i:i+k-1])
        nodes.add(st[i+1:i+k])
    return nodes, edges

# nodes, edges = de_bruijn_ize("ACGCGTCG", 3)

# Visualize - must do in jupyter

# EULERIAN WALK FUNCTION?
