""" Communicating with Outside 1 """
#f = open('myfile', 'r') # reading is default
#f = open('myfile', 'w') # write
#f = open('myfile', 'a') # append

# use try except -
# try:
#     f = open('myfile')
# except IOError:
#     print "File doesn't exist."

# for line in f - each line
# f.read() - end of file
# f.seek(0) - returns to position 0 in the file
# THEN use f.read() - returns entire file
# f.readline() just reads a line

# f.write() writes the string to a file (either overwrites or appends)
# need f.close()

""" Communicating with Outside 2 """
# all about FASTA files
# header and then sequence and then maybe aditional sequences
# WANT TO BUILD A DICTIONARY of FASTA files
# open
# read one line at a time
    # is it a header?
        # yes: add new
        # no: update sequence
# close

def fastaread(filename):
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

""" Communicating with Outside 3 """
# retrieve keys/values from dictionary using items
# for name, seq in seq.items():
#   print(name, seq)

import sys
# filename = sys.argv[1]
# print fastaread(filename)

# sys.stdin.read() - returns what you type
# type until Ctrl-D
#print sys.stdin.read()
# similar for stdout.write()

# Interfacing with outside programs
# Want to call external programs on different files
# Use call/execute from within script
    # import subprocess
    # use call()
    # EX: use for tophat

# Question 1: f=open('myfile', 'a')
# Question 2: A, B, D only
# Question 3: 1 and 3, 1 only ** WRONG
    # options: 2 only, none, 3 only
# Question 4: myfile1.fa
# Question 5: error saying file doesn't exist

def get_extension1(filename):
    return(filename.split(".")[-1])

def get_extension2(filename):
    import os.path
    return(os.path.splitext(filename)[1])

def get_extension3(filename):
    return filename[filename.rfind('.'):][1:]

print get_extension1("myfile.tar.gz")
print get_extension1("myfile.tar.gz.py")

print get_extension2("myfile.tar.gz")
print get_extension2("myfile.tar.gz.py")
