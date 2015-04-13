# format file --> strip white space and separate by spaces
# for x in range(len(line))
# check to see if word in dictionary already
# if not in dictionary, add it with a value of 1
# dictionary[word] += 1
# print each unique key and its value / count

words_and_counts = {}

text_file = open("test.txt")
for line in text_file:
    words_in_line = line.rstrip().split(" ")
    print words_in_line