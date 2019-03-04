# !/usr/bin/env python

import os
import re
import sys

current_file = None
current_index = 0

stopwords = ["and", "but", "is", "the", "to"]

# input comes from STDIN (standard input)
for line in sys.stdin:

    # remove leading and trailing whitespace
    line = line.strip().lower()
    line = re.sub(r'[^\w\s]',' ',line)
    # get the doc identifier
    docId = os.environ["map_input_file"]

    if docId != current_file:
        current_file = docId
        current_index = 0
    # split the line into words
    words = line.split()

    # increase counters
    for word in words:
        current_index += 1
        if (word.isdigit()) | (word in stopwords): continue
        print(word + '\t' + current_file + '\t' + str(current_index))