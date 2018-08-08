# https://www.hackerrank.com/challenges/alternating-characters/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=strings

# You are given a string containing characters  and  only. Your task is to change it into a string such that there are no matching adjacent characters. To do this, you are allowed to delete zero or more characters in the string.
#
# Your task is to find the minimum number of required deletions.
#
# For example, given the string , remove an  at positions  and  to make  in  deletions.
#
# Function Description
#
# Complete the alternatingCharacters function in the editor below. It must return an integer representing the minimum number of deletions to make the alternating string.
#
# alternatingCharacters has the following parameter(s):
#
# s: a string
# Input Format
#
# The first line contains an integer , the number of queries.
# The next  lines each contain a string .
#
# Constraints
#
# Each string  will consist only of characters  and
# Output Format
#
# For each query, print the minimum number of deletions required on a new line.
#
# Sample Input
#
# 5
# AAAA
# BBBBB
# ABABABAB
# BABABA
# AAABBB
# Sample Output
#
# 3
# 4
# 0
# 0
# 4

#!/bin/python

import math
import os
import random
import re
import sys

# Complete the alternatingCharacters function below.
def alternatingCharacters(s):
    index = 1
    count = 0
    while (index < len(s)):
        if (s[index-1] == s[index]):
            count+=1
        index+=1
    return count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(raw_input())

    for q_itr in xrange(q):
        s = raw_input()

        result = alternatingCharacters(s)

        fptr.write(str(result) + '\n')

    fptr.close()


#solution works!
