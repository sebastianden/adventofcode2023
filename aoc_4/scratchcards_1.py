# Answer: 20407

with open("input.txt") as f:
    data = f.read().splitlines()

value_list = []
for line in data:
    numbers = line.split(':')[1]
    card_numbers = [i for i in numbers.split('|')[0].split(' ') if i != '']
    winning_numbers = [i for i in numbers.split('|')[1].split(' ') if i != '']

    value = 0
    for i in card_numbers:
        if i in winning_numbers:
            if value == 0:
                value += 1
            else:
                value *= 2
    value_list.append(value)
print(sum(value_list))
