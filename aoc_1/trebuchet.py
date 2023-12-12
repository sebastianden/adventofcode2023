# Answers:
# 1.1: 54708
# 1.2: 54087

import re

# Convert words to integers
int_map = {
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9'
}

with open('input.txt') as f:
    # Read lines wihout newline character
    lines = [line.rstrip() for line in f]

index_list = []

# Go through each word and save the digit and it's index
for line in lines:
    local_index_list = []
    # First save indices of words to be replaced with integers
    for word in int_map:
        if word in line:
            for index in [m.start() for m in re.finditer(word, line)]:
                local_index_list.append((int_map[word], index))
    # Save actual digits to the same local list
    for i, letter in enumerate(line):
        if letter.isdigit():
            local_index_list.append((letter, i))
    index_list.append(local_index_list)

# For each sublist, take the element with the lowest and the one with the
# highest index
sum = 0
for sub_list in index_list:
    sum += int(min(sub_list, key=lambda x: x[1])[0] + max(sub_list, key=lambda x: x[1])[0])
print(sum)
