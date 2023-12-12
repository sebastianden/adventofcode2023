# Answer: 23806951

with open("input.txt") as f:
    data = f.read().splitlines()

card_list = [1] * len(data)

for n, line in enumerate(data):
    numbers = line.split(':')[1]
    card_numbers = [i for i in numbers.split('|')[0].split(' ') if i != '']
    winning_numbers = [i for i in numbers.split('|')[1].split(' ') if i != '']

    matches = 0
    for i in card_numbers:
        if i in winning_numbers:
            matches += 1

    for m in range(1, matches+1):
        card_list[n+m] = card_list[n+m] + card_list[n]
    print(card_list)


print(sum(card_list))
