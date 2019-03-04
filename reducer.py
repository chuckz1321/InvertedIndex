from operator import itemgetter
import sys

current_word = None
wordDic = {}
word = None
output = {}

# input comes from STDIN
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()

    # parse the input we got from mapper.py
    word, docId, position = line.split('\t', 2)

    # convert count (currently a string) to int
    try:
        position = int(position)
    except ValueError:
        # count was not a number, so silently
        # ignore/discard this line
        continue

    if word != current_word:
        current_word = word
        output[word] = {}

    if docId not in output[word].keys():
        output[word][docId] = []
    output[word][docId].append(position)

for key in output.keys():
    for doc in output[key].keys():
        output[key][doc].sort()

for key in output.keys():
    outStr = {}
    outStr[key] =output[key]
    print(outStr)