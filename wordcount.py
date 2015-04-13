# Counts number of times a word occurs in the text file 
# Accounts for punctuation and case
# Can call specified file from command line

import sys

words_and_counts = {}

text_filename = sys.argv[1]
text_file = open(text_filename)

for line in text_file:
    words_in_line = line.rstrip().split(" ")
    lower_words = [word.lower().rstrip(",.?!;:") for word in words_in_line]

    for word in lower_words:
        if word in words_and_counts:
            words_and_counts[word] += 1
        else:
            words_and_counts[word] = 1

for word, count in words_and_counts.items():
    print word, count