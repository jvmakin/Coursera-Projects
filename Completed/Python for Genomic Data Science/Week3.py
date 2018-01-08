"""Quiz 5"""

# Question 1: Functions swap2, swap3, and swap4 only
# Question 2: When x is 0 or positive
# Question 3:
    # function1 produces the output:
    # 3
    # 2
    # 1
    # and function2 runs infinitely.
# Question 4: x+n*y

# compute(3, 4, 2)
# compute(2, 6, 2)
# compute(1, 8, 2)
# compute(0, 10, 2)
# x = n*y + x = (3*2) + 4

# Question 5: never return a value
# Question 6: valid_dna4 only
    # a is wrong (returns based on first)
    # b is always true
    # c is only false if the last letter is WRONG
    # d works!
# Question 7: in common w/o duplicates
# Question 8: error
# Question 9: may have no parameters
# Question 10: only C

"""Quiz 6"""
# Question 1:
    # ONLY
    # import sys
    # print(sys.version) - yep
# Question 2: Creates a dna variable containing a string of length 1000000, and with the a,c,g,t characters.
# Question 3: all work!
# Question 4: count 4, see below
# Question 5: A, B, D
# Question 6
import time
print dir(time)


# import random
# import time
#
# def create_dna(n, alphabet='acgt'):
#     return ''.join([random.choice(alphabet) for i in range(n)])
# dna = create_dna(1000000)
# def count1(dna, base):
#     i = 0
#     for c in dna:
#         if c == base:
# 	    i += 1
#     return i
#
# def count2(dna, base):
#     i = 0
#     for j in range(len(dna)):
#         if dna[j] == base:
# 	    i += 1
#     return i
#
# def count3(dna, base):
#     match = [c == base for c in dna]
#     return sum(match)
#
# def count4(dna, base):
#     return dna.count(base)
#
# def count5(dna, base):
#     return len([i for i in range(len(dna)) if dna[i] == base])
#
# def count6(dna,base):
#     return sum(c == base for c in dna)
#
# t0 = time.clock()
# count1(dna, 'a')
# print time.clock() - t0
# t0 = time.clock()
# count2(dna, 'a')
# print time.clock() - t0
# t0 = time.clock()
# count3(dna, 'a')
# print time.clock() - t0
# t0 = time.clock()
# count4(dna, 'a')
# print time.clock() - t0
# t0 = time.clock()
# count5(dna, 'a')
# print time.clock() - t0
# t0 = time.clock()
# count6(dna, 'a')
# print time.clock() - t0
