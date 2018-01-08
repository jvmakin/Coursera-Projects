# Quiz 4
# - Question 1
(rnatype is 'ncRNA' and length>=200) or (rnatype is 'ncRNA' and length==22)
# negate
# not(1) and not(2)
# (rnatype is NOT 'ncRNA' and length < 200) AND (rnatype is NOT 'ncRNA' and length != 22)
# rnatype is not ncRNA and length <200 and not 22

# - Question 2
if fold > 2 : print(’condition A’)
# to skip, must be less than 2
elif fold>100: print(’condition B’)
# can't print here then
if fold> 2 or fold<2 : print('condition A')
# must = 2
else : print(’condition B’)

# For what values of the variable fold would the following code print ‘condition B’?

# - Question 3
# How many times does this print?
i=1
while i< 2048 :
      i=2*i
# 2^11 = 2048, 11 times

# - Question 4
# What sequence of numbers does the range(1,-23,-3) expression evaluate to?
# 1 down by -3 to 20

# - Question 5
for i in range(len(seq)) :     # line 1
        for j in range(i) :        # line 2
                print(seq[j:i])

# - Question 6
i=0
while i<len(seq) :
      j=0
      while(j<i) :
                print(seq[j:i])
                j+=1
      i+=1

# - Question 7
# Change line 3

# - Question 8
# version 2 is not computing result



# Question 1 - WRONG
rnatype is not 'ncRNA' or ( length <200 and length != 22)
#(rnatype is not 'ncRNA' and length < 200) or (rnatype is not 'ncRNA' and length != 22)
#(rnatype is not 'ncRNA' and length < 200) and (rnatype is not 'ncRNA' and length != 22)
rnatype is not 'ncRNA and length > 22
# Question 2: if fold is 2
# Question 3: 11
# Question 4: 1, -2, -5, -8, -11, -14, -17, -20
# Question 5: Only B
    #Change line 1 to:

    #for i in range(len(seq)+1) :
# Question 6: Only C
# Question 7: Change line3 to be:
    # if elem in L2 and elem not in L3:
# Question 8: The value of the result variable is the same, but the variable d is different.
# Question 9: for no value
# Question 10: 2
