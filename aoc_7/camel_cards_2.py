# Answer: 250057090

from enum import Enum

card_labels = ['A', 'K', 'Q', 'T', '9', '8', '7', '6', '5', '4', '3', '2', 'J']
card_map = {k: 14-v for v, k in enumerate(card_labels)}


class HandType(Enum):
    HIGH_CARD = 0
    ONE_PAIR = 1
    TWO_PAIR = 2
    THREE_OF_A_KIND = 3
    FULL_HOUSE = 4
    FOUR_OF_A_KIND = 5
    FIVE_OF_A_KIND = 6


def get_hand_type(hand_map):
    n_jokers = hand_map.pop('J')

    # Cover the case where we have 3, 4 or 5 jokers
    if n_jokers + max(hand_map.values()) == 5:
        return HandType.FIVE_OF_A_KIND
    elif n_jokers + max(hand_map.values()) == 4:
        return HandType.FOUR_OF_A_KIND
    # Cover the cases where we have 1 or 2 jokers

    # Can only have a full house with jokers if we have two pairs already
    elif (3 in hand_map.values() and 2 in hand_map.values()) or (list(hand_map.values()).count(2) == 2 and n_jokers == 1):
        return HandType.FULL_HOUSE
    elif (3 in hand_map.values()) or (2 in hand_map.values() and n_jokers == 1) or n_jokers == 2:
        return HandType.THREE_OF_A_KIND
    # Cannot have a two pair with jokers (would count as three of a kind at least)
    elif list(hand_map.values()).count(2) == 2:
        return HandType.TWO_PAIR
    elif list(hand_map.values()).count(2) == 1 or n_jokers == 1:
        return HandType.ONE_PAIR
    else:
        return HandType.HIGH_CARD


def rank_hands_by_highest_card(hand_range, card_loc):
    hand_range = sorted(hand_range, key=lambda x: card_map[x[1][card_loc]])
    ranked_hands = []
    m = 0
    n = 0
    for hand in hand_range:
        if n + 1 >= len(hand_range) or hand[1][card_loc] != hand_range[n+1][1][card_loc]:
            if n - m > 0:
                ranked_hands[m:n+1] = rank_hands_by_highest_card(hand_range[m:n+1], card_loc+1)
            else:
                ranked_hands.append(hand)
            m = n + 1
        n += 1
    return ranked_hands


with open('input.txt', 'r') as f:
    example_input = f.read().splitlines()

hands = []
for line in example_input:
    hands.append((list(line.split(' ')[0]), int(line.split(' ')[1])))

# Find the hand type for each hand
results = []
for hand in hands:
    hand_map = {k: 0 for k in card_labels}
    for card in hand[0]:
        hand_map[card] += 1
    hand_type = get_hand_type(hand_map)
    results.append((hand_type, hand[0], hand[1]))


# Sort by hand type
results = sorted(results, key=lambda x: x[0].value)

# Go through the hands
ranked_hands = []
i = 0
j = 0
for hand in results:
    if j + 1 >= len(results) or hand[0] != results[j+1][0]:
        if j - i > 0:
            ranked_hands[i:j+1] = rank_hands_by_highest_card(results[i:j+1], 0)
        else:
            ranked_hands.append(results[i])
        i = j + 1
    j += 1


# Calculate the winnings
total_winnings = [hand[2] * (i+1) for i, hand in enumerate(ranked_hands)]
print("-----------------TOTAL WINNINGS-----------------")
print(sum(total_winnings))
