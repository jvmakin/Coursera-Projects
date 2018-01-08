
""" Finds longest common prefix between two strings """
def longestCommonPrefix(s1, s2):
    i = 0
    while i < min(s1, s2) and s1[i] == s2[i]:
        i += 1
    return s1[:i]

""" Finds reverse complement of DNA string"""
def reverseComplement(s):
    complement = {'A':'T', 'T':'A', 'C':'G', 'G':'C'}
    rev = ''
    for i in range(len(s) - 1, -1, -1):
        rev += complement[s[i]]
    return rev

""" Reads and returns genome from a FASTA file """
def readGenome(filename):
    genome = ''
    with open(filename, 'r') as f:
        for line in f:
            if not line[0] == '>':
                genome += line.rstrip()
    return genome

""" Reads fastQ files and returns sequences/quality scores """
def readFastq(filename):
    sequences = []
    qualities = []
    with open(filename) as fh:
        while True:
            fh.readline() # skip name line
            seq = fh.readline().rstrip() # read base sequence
            fh.readline() # skip placeholder line
            qual = fh.readline().rstrip() #base quality line
            if len(seq) == 0:
                break
            sequences.append(seq)
            qualities.append(qual)
    return sequences, qualities
