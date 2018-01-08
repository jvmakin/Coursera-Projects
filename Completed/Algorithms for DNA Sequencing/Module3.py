# from pandas import *
# print DataFrame(D)

# LECTURE: Finding Distances
def hammingDistance(x,y):
    nmm = 0
    for i in xrange(0, len(x)):
        if x[i] != y[i]:
            nmm += 1
    return nmm

# PRACTICAL: Implementing DP for Edit Distance

# Input: Strings X, Y
# Output: Edit Distance b/w X, Y
# Calculated using dynamic programming
def editDistance(x, y):
    D = []

    # Create x+1 by y+1 matrix of zeroes
    for i in range(len(x)+1):
        D. append([0]*(len(y) + 1))

    # Fill in for empty string (first row/column)
    for i in range(len(x) +1):
        D[i][0] = i
    for i in range(len(y) +1):
        D[0][i] = i

    for i in range(1, len(x)+1):
        for j in range(1, len(y) + 1):
            distHor = D[i][j-1] + 1
            distVer = D[i-1][j] + 1
            if x[i-1] == y[j-1]:
                distDiag = D[i-1][j-1]
            else:
                distDiag = D[i-1][j-1] + 1
            D[i][j] = min(distHor, distVer, distDiag)

    return D[-1][-1]

# PRACTICAL: Implementing global alignment

alphabet = ['A', 'C', 'G', 'T']
# Penalty matrix - skip is 8
score = [[0, 4, 2, 4, 8],
         [4, 0, 4, 2, 8],
         [2, 4, 0, 4, 8],
         [4, 2, 4, 0, 8],
         [8, 8, 8, 8, 8]]

# Input: Strings X, Y
# Output: Edit Distance b/w X, Y using penalty matrix
# Global Alignment calculated using dynamic programming
def globalAlignment(x, y):
    D = []
    # SAME: Create x+1 by y+1 matrix of zeroes
    for i in range(len(x)+1):
        D. append([0]*(len(y) + 1))

    # DIFFERENT: initialize first row/column
    for i in range(1, len(x) +1):
        D[i][0] = D[i-1][0] + score[alphabet.index(x[i-1])][-1]
    for i in range(1, len(y) +1):
        D[0][i] = D[0][i-1] + score[-1][alphabet.index(y[i-1])]

    # DIFFERENT
    for i in range(1, len(x)+1):
        for j in range(1, len(y) + 1):
            distHor = D[i][j-1] + score[-1][alphabet.index(y[j-1])]
            distVer = D[i-1][j] + score[alphabet.index(x[i-1])][-1]
            if x[i-1] == y[j-1]:
                distDiag = D[i-1][j-1]
            else:
                distDiag = D[i-1][j-1] + score[alphabet.index(x[i-1])][alphabet.index(y[j-1])]
            D[i][j] = min(distHor, distVer, distDiag)

    return D[-1][-1]

# PRACTICAL: OVERLAPS BETWEEN PAIRS OF READS
# Finds overlapping suffix of a, prefix of b
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

# PRACTICAL: Finding and representing all overlaps

from itertools import permutations
#print list(permutations([1,2,3], 2)) # [(1, 2), (1, 3), (2, 1), (2, 3), (3, 1), (3, 2)]

# Create naive overlap map
def naive_overlap_map(reads, k):
    olaps = {}
    for a, b in permutations(reads, 2):
        olen = overlap(a, b, min_length=k)
        if olen > 0:
            olaps[(a, b)] = olen
    return olaps

reads = ['ACGGATGATC', 'GATCAAGT', 'TTCACGGA']
print naive_overlap_map(reads, 3)
