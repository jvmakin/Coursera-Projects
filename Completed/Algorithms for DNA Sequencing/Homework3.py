from pandas import *
def readGenome(filename):
    genome = ''
    with open(filename, 'r') as f:
        for line in f:
            # ignore header line with genome information
            if not line[0] == '>':
                genome += line.rstrip()
    return genome

def editDistance(x, y):
    # Create distance matrix
    D = []
    for i in range(len(x)+1):
        D.append([0]*(len(y)+1))
    # Initialize first row and column of matrix
    for i in range(len(x)+1):
        D[i][0] = i
    # THIS CHANGES
    for i in range(len(y)+1):
        D[0][i] = 0
    # Fill in the rest of the matrix
    for i in range(1, len(x)+1):
        for j in range(1, len(y)+1):
            distHor = D[i][j-1] + 1
            distVer = D[i-1][j] + 1
            if x[i-1] == y[j-1]:
                distDiag = D[i-1][j-1]
            else:
                distDiag = D[i-1][j-1] + 1
            D[i][j] = min(distHor, distVer, distDiag)

    print DataFrame(D)
    distance = D[-1]
    distance.sort()
    return distance[0]

T = readGenome('chr1.GRCh38.excerpt.fasta')

# Question 1: 3
# P = 'GCTGATCGATCGTACG'
# print editDistance(P,T)

# Question 2: 2
# P = 'GATTTACCAGATTGAG'
# print editDistance(P,T)

def readFASTQ(filename):
    f = open(filename)
    reads = []
    while True:
        h = f.readline()
        if len(h) == 0:
            break
        sequence = f.readline().rstrip()
        _ = f.readline()
        quality = f.readline().rstrip()
        reads.append(sequence)

    return reads

def overlap(a, b, min_length=3):
    """ Return length of longest suffix of 'a' matching
        a prefix of 'b' that is at least 'min_length'
        characters long.  If no such overlap exists,
        return 0. """
    start = 0  # start all the way at the left
    while True:
        start = a.find(b[:min_length], start)  # look for b's prefix in a
        if start == -1:  # no more occurrences to right
            return 0
        # found occurrence; check for full suffix/prefix match
        if b.startswith(a[start:]):
            return len(a)-start
        start += 1  # move just past previous match

def overlap_all_pairs(reads, k):
    olaps = {}

    # Let every k-mer in dataset have associated python set object which starts empty
    # Python dictionary to associate each k-mer with corresponding set
    # 1. For every k-mer in a read, add the read to the set object corresponding to that kmer
    kmer_dict = {}
    for read in reads:
        for i in range(len(read)-k+1):
            kmer_dict[read[i:i+k]] = set()
    for read in reads:
        for i in range(len(read)-k+1):
            kmer_dict[read[i:i+k]].add(read)

    # 2. For each read a, we find all overlaps involving a suffix of a
    # Take a's length-k suffix and find all reads containing that kmer THEN call overlap

    for read in reads:
        kmers = kmer_dict[read[-1*k:]]
        for kmer_read in kmers:
            if read != kmer_read:
                olen = overlap(read, kmer_read, min_length=k)
                if olen > 0:
                    olaps[(read, kmer_read)] = olen
    return olaps

# # Question 3: 904746
# file = 'ERR266411_1.for_asm.fastq'
# reads = readFASTQ(file)
# overlaps = overlap_all_pairs(reads, 30)
# print len(overlaps)
#
# # Question 4:
# s = set()
# for a, b in overlaps.keys():
#     s.add(a)
# print len(s)

# reads = readFASTQ('ads1_week4_reads.fq')
# overlaps = overlap_all_pairs(reads, 25)
# print overlaps

read = 'AAATACGTT'
print read.count('A')
print read.count('T')
