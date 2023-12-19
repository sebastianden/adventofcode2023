# Answer: 136146366355609

from functools import reduce
import copy


def parse_input(data):
    workflows = {}

    while data:
        line = data.pop(0)
        if line == "":
            break

        workflow_name = line.split("{")[0]
        workflow_rules = line.split("{")[1].split("}")[0].split(",")
        workflows[workflow_name] = workflow_rules
    return workflows


def update_state(state, rule, default=False):
    # Parse the rule
    condition = rule.split(':')[0]
    category = condition[0]
    operator = condition[1]
    value = int(condition[2:])

    if operator == ">":
        # Maybe there is something with exclusive ranges?
        state[category].append((1, value + 1) if default else (value + 1, 4001))
    elif operator == "<":
        state[category].append((value, 4001) if default else (1, value))

    return state


def calc_total_possibilities(state):
    p = 1
    for key, value in state.items():
        ranges = [set(range(start, end)) for start, end in value]
        p *= len(set.intersection(*ranges))
    return p


def get_combinations(state, node, workflows):
    if node == "A":
        return calc_total_possibilities(state)
    if node == "R":
        return 0
    else:
        # Keep track of the state AND default state at the same time
        default_state = copy.deepcopy(state)
        combinations = []
        for rule in workflows[node]:
            if ':' in rule:
                new_state = copy.deepcopy(default_state)
                # Update state and default state according to the rule
                new_state = update_state(new_state, rule)
                default_state = update_state(default_state, rule, True)
                # Dont only modify the default state! also the other ones!!!

                combinations.append(get_combinations(new_state, rule.split(':')[1], workflows))
            # Go the path of the default rule
            else:
                default_rule = rule
                combinations.append(get_combinations(default_state, default_rule, workflows))
        return sum(combinations)


if __name__ == "__main__":
    with open("input.txt") as f:
        data = f.read().splitlines()

    workflows = parse_input(data)

    # print(workflows)

    init_state = {
        "x": [(1, 4001)],
        "m": [(1, 4001)],
        "a": [(1, 4001)],
        "s": [(1, 4001)],
    }

    print(get_combinations(init_state, 'in', workflows))
