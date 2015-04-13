# Counts number of times a word occurs in the text file 
# Accounts for punctuation and case
# Can call specified file from command line
# Uses collections.Counter

import sys
from collections import Counter

words_and_counts = Counter()

text_filename = sys.argv[1]
text_file = open(text_filename)

for line in text_file:
    words_in_line = line.rstrip().split(" ")
    lower_words = [word.lower().rstrip(",.?!;:") for word in words_in_line]

    for word in lower_words:
        words_and_counts[word] += 1

for word, count in words_and_counts.items():
    print word, count