import sys
import getopt
def usage():
    print """
processfasta.py: reads a FASTA file and build a dictionary
with all sequences  bigger than a given length

processfasta.py [-h] [-l <length>] <filename>

-h              print this message
-l <length>     filter all sequences with a length
                smaller than <length>
                (default <length>=0)
<filename>      the file has to be in FASTA format
"""

# o = list of optional arguments
# a = list of requirements
# not including filename
# optional : l:h - colon after l b/c it requires a value

o, a = getopt.getopt(sys.argv[1:], 'l:h')
opts = {}
seqlen = 0;

for k,v in o:
    opts[k] = v
# help message
if '-h' in opts.keys():
    usage(); sys.exit() #print message, exit
if len(a) < 1:
    usage(); sys.exit("Input FASTA file is missing.")
if '-l' in opt.keys():
    if int(opts['1'])<0 :
        print "Length of sequence should be positive!"; sys.exit(0)
    seqlen=opts['-l']
# Standard streams:
# stdin from keyboard or piped from another program
# stdout is the stream where program writes its output data
# stderr is another output stream used by programs to output error/diagnostics

#EX: my_program | my_script.sh 1>program_output.txt...
