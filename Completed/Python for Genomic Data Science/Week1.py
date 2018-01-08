# This makes file executable
# must run "chmod a+x Week1.py" first
#!/usr/bin/python

# Lecture 2.2
""" Here is my comment """
dna = "acgctcgcgcggcgatagctgatcgatcggcgcgctttttttttaaaag"
# count number of "c" in str
print dna.count( 'c' )
# find first occurence (from 0) of "ag"
print dna.find("ag")
# find last occurence of "ag"
print dna.rfind("ag")
# replace "a" with "A"
print dna.replace("a", "A")

# Lecture 2.3 - calculating GC content
# Read DNA sequence from user
dna = "acgctcgcgcggcgatagctgatcgatcggcgcgctttttttttaaaag"
# Count # of C's in DNA sequence
no_c = dna.count("c")
# Count # of G's in DNA sequence
no_g = dna.count("g")
# Find length
dna_length = len(dna)
# Get GC content
gc_percent = (no_c + no_g)*100.0/dna_length
print gc_percent

# Lecture 2.4
# in python 3, use input
#dna = raw_input("Enter DNA sequence, please: ")

# output formatting
print "The DNA sequence's GC content is", gc_percent, "%"
# %5.3f ..." %
# % indicates formatting string, 5 is total number of digits,
# following number is number of digits after the dot, f indicates the type
print "The DNA sequence's GC content is %5.3f %%" % gc_percent

# other examples
print "%d" % 10.6 # turn into integer - 10
print "%3d" % 10.6 # adds a space in front of 10 b/c 3 characters before decimal
print "%o" % 10 # turns into hexadecimal integer (???) 12
print "%e" % 10.6 # scientific notation
