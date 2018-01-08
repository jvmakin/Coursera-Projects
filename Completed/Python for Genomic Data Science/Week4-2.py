# PROBLEM: find out what species an unknown DNA sequence came from


# QUIZ 8
# Question 1: Bio.Blast.NCBIWWW
# Question 2: FastaIO
# Question 3:
# from Bio.Blast import NCBIWWW
# fasta_string = "TGGGCCTCATATTTATCCTATATACCATGTTCGTATGGTGGCGCGATGTTCTACGTGAATCCACGTTCGAAGGACATCATACCAAAGTCGTACAATTAGGACCTCGATATGGTTTTATTCTGTTTATCGTATCGGAGGTTATGTTCTTTTTTGCTCTTTTTCGGGCTTCTTCTCATTCTTCTTTGGCACCTACGGTAGAG"
# result_handle = NCBIWWW.qblast("blastn", "nt", fasta_string)
# blast_result = open("my_blast.xml", "w")
# blast_result.write(result_handle.read())
# blast_result.close()
# result_handle.close()

# Hyosyamus niger, Capsicum annuum, *Nicotiana tabacum, Solanum pennellii

# Question 4
from Bio.Seq import Seq
#my_seq = Seq("TATACCC")
# *print my_seq.reverse_complement()
#print complement(my_seq.reverse())
#print reverse(my_seq.complement())
#print my_seq.reverse()

# Question 5
my_seq = Seq("TGGGCCTCATATTTATCCTATATACCATGTTCGTATGGTGGCGCGATGTTCTACGTGAATCCACGTTCGAAGGACATCATACCAAAGTCGTACAATTAGGACCTCGATATGGTTTTATTCTGTTTATCGTATCGGAGGTTATGTTCTTTTTTGCTCTTTTTCGGGCTTCTTCTCATTCTTCTTTGGCACCTACGGTAGAG")
print my_seq.translate()
