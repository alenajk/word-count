# Counts number of times a word occurs in the text file. 
# Does not account for punctuation.

words_and_counts = {}

text_file = open("test.txt")

for line in text_file:
    words_in_line = line.rstrip().split(" ")
    for word in words_in_line:
        if word in words_and_counts:
            words_and_counts[word] += 1
        else:
            words_and_counts[word] = 1

for word, count in words_and_counts.items():
    print word, count