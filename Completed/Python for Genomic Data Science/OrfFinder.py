import re

""" Module to read/parse a FASTA file and then create ORFs from it """

# Input: filename of a FASTA file
# Output: dictionary of {gene id: gene sequence}
def fasta_read(filename):
    try:
        f = open(filename, 'r')
    except IOError:
        print "No such file!"

    seqs = {}
    for line in f:
        line = line.rstrip()
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

SEQS = fasta_read('dna.example.fasta')

# Input: sequence
# Output: dicitonary of ORFs by reading frame, {1: ORF, 2: ORF...}
def orf_finder(my_seq):
    start = 'ATG'
    stops = ['TAG', 'TAA', 'TGA']

    fwd_start_codons = [x.start() for x in re.finditer(start, my_seq)]
    print [x%3 for x in fwd_start_codons]
    orfs = {}

    # for frame in range(1,4):
    #
    #     seq = my_seq[frame-1:]
    #     codons = re.findall('...', seq)
    #     if not start in codons:
    #         continue
    #     start_pos = [i for i,val in enumerate(codons) if val==start]
    #
    #     pos = min(start_pos)
    #
    #     while pos < len(codons):
    #
    #         orf = codons[pos]
    #         j = pos + 1
    #         while not codons[j] in stops and j < len(codons)-1:
    #             orf += codons[j]
    #             j += 1
    #         if codons[j] in stops:
    #             orf += codons[j]
    #             if frame in orfs.keys():
    #                 orfs[frame] += [orf]
    #             else:
    #                 orfs[frame] = [orf]
    #
    #             if len(filter(lambda x: x>j+1, start_pos)) == 0:
    #                 break
    #             pos = min(filter(lambda x: x>j+1, start_pos))
    #         else:
    #             break
    #
    # return orfs

test = SEQS["gi|142022655|gb|EQ086233.1|43"]
orf_finder(test)


# def main():
#
# if __name__ == '__main__':
#     main()
