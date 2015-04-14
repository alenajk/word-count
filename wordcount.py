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

#Initializing new dictionary
new_dict = {}

#Made count the keys to the dictionary
#Made all the words with that count into a list of strings as the value
for word_count_tuple in words_and_counts.most_common():
    word, number = list(word_count_tuple)
    if number in new_dict:
        new_dict[number].append(word)
    else:
        new_dict[number] = [word]

#Sorted each list of values (words) so that they are alphabetized
key_list = new_dict.keys()
for key in key_list:
    new_dict[key] = sorted(new_dict[key])

#Sorted the key (number) list so that it reads highest to lowest
sorted_key_list = sorted(key_list)[::-1]

#Print output
for i in sorted_key_list:
    for w in new_dict[i]:
        print w, i