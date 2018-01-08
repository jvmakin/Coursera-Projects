from Bio.Seq import Seq
import re
from collections import Counter
# opens FASTA, returns dictionary of FASTA files
def fastaread(filename):
    try:
        f = open(filename, 'r')
    except IOError:
        print "No such file!"

    seqs = {}
    for line in f:
        line = line.rstrip().upper()
        if len(line) == 0:
            continue
        elif line[0] == '>':
            words = line.split()
            name = words[0][1:]
            seqs[name] = ''
        else:
            seqs[name] = seqs[name] + line
    f.close()
    return seqs

TEST_FILENAME = 'dna2.fasta'
TEST_SEQS = fastaread(TEST_FILENAME)
# 1 - How many records
# print len(TEST_SEQS)

# 2   - What are the lengths of the sequences in the file?
    # - What is the longest? What is the shortest?
    # - Is there more than one longest/shortest?
    # - What are their identifiers

def lengthconverter(seq_dict):
    len_dict = {}
    for key in seq_dict.keys():
        len_dict[key] = len(seq_dict[key])
    for key, value in sorted(len_dict.iteritems(), key=lambda (k,v): (v,k)):
        print "%s: %s" % (key, value)

#lengthconverter(TEST_SEQS)

# 3 - want to identify sequence with longest ORF
# Given an input reading frame on the forward strand (1, 2, 3)

# Returns longest orf and frame position
def orf_finder(my_seq):
    start = 'ATG'
    stops = ['TAG', 'TAA', 'TGA']

    orfs = {}
    for frame in range(1,4):
        seq = my_seq[frame-1:]
        codons = re.findall('...', seq)
        if not start in codons:
            continue
        start_pos = [i for i,val in enumerate(codons) if val==start]

        pos = min(start_pos)

        while pos < len(codons):

            orf = codons[pos]
            j = pos + 1
            while not codons[j] in stops and j < len(codons)-1:
                orf += codons[j]
                j += 1
            if codons[j] in stops:
                orf += codons[j]
                if frame in orfs.keys():
                    orfs[frame] += [orf]
                else:
                    orfs[frame] = [orf]

                if len(filter(lambda x: x>j+1, start_pos)) == 0:
                    break
                pos = min(filter(lambda x: x>j+1, start_pos))
            else:
                break

    return orfs

# Dict: {id: {frame: orfs, frame:orfs}}

TEST_ORFS = {}
for seq_id in TEST_SEQS.keys():
    TEST_ORFS[seq_id] = orf_finder(TEST_SEQS[seq_id])

# max_len = 0
# name = ''
# for seq_id in TEST_ORFS.keys():
#     if 3 in TEST_ORFS[seq_id].keys():
#         orfs_2 = TEST_ORFS[seq_id][3]
#         for orf in orfs_2:
#             if len(orf) > max_len:
#                 max_len = len(orf)
#                 name = seq_id
#
# print max_len, name

# 1821 gi|142022655|gb|EQ086233.1|527
# long_orf = [item for item in TEST_ORFS['gi|142022655|gb|EQ086233.1|527'][3] if len(item) == 1821][0]
# orf_seq = TEST_SEQS['gi|142022655|gb|EQ086233.1|527']
# print orf_seq.find(long_orf)

# max_len = 0
# name = ''
# for seq_id in TEST_ORFS.keys():
#     for i in range(1,4):
#         if i in TEST_ORFS[seq_id].keys():
#             print i
#             orfs_2 = TEST_ORFS[seq_id][i]
#             for orf in orfs_2:
#                 if len(orf) > max_len:
#                     max_len = len(orf)
#                     name = seq_id
# print max_len, name
#
# orfer = TEST_ORFS['gi|142022655|gb|EQ086233.1|16']
# max_len = 0
# for frame in orfer.keys():
#     frame_orfs = orfer[frame]
#     for orf in frame_orfs:
#         if len(orf) > max_len:
#             max_len = len(orf)
# print max_len


# 4 - Identifying repeats
# returns all repeats of length n in a sequence in dictionary form
def find_repeats(sequence, n):
    # n possible starting positions
    rep_dict = {}
    seqs = [sequence[i:] for i in range(0, n)]
    for seq in seqs:
        repeats = re.findall('.'*n, seq)
        for rep in repeats:
            if rep in rep_dict.keys():
                rep_dict[rep] = rep_dict[rep] + 1
            else:
                rep_dict[rep] = 1
    return rep_dict

# same as above but for a seq dict - only returns > 1
def repeats_file(seq_dict, n):
    seqs = seq_dict.values()
    file_dict = {}
    i = 0
    for seq in seqs:
        seq_repeats = find_repeats(seq, n)
        A = Counter(seq_repeats)
        B = Counter(file_dict)
        file_dict = A+B
    return dict(filter(lambda (a,b): b > 1, file_dict.items()))


TEST_REPEATS = repeats_file(TEST_SEQS, 7)
print TEST_REPEATS


# # Identify all repeats of given length in FASTA
# print sum(TEST_REPEATS.values())
# # Determine how many time repeat occurs in file
# # Most frequent repeat of a given length
max_rep = max(TEST_REPEATS.values())
print max_rep
num_reps = 0
for key in TEST_REPEATS.keys():
    if TEST_REPEATS[key] == max_rep:
        print key
        num_reps += 1
