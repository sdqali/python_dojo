#! /usr/bin/env python


# Fast look up for word occurrence using collections.Counter
# A good test will be to run this against the mthesaur.txt file from http://maximilk.web.fc2.com/data/readme_moby.htm

from collections import Counter
import re
import datetime
import sys

word_to_count = sys.argv[1]
input_file = sys.argv[2]

counter =  Counter([])

with open(input_file) as f:
    inp = f.read()
    words = re.split("\W+", inp)
    print("Total words: %s" % len(words))

    start_time = datetime.datetime.now()
    counter.update(words)
    end_time = datetime.datetime.now()
    delta = end_time - start_time
    print("Time spent updating the counter: %s" % delta)

print("Word '%s' occurred %s times." % (word_to_count, counter[word_to_count]))
