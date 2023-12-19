# Answer: 434147
import re


def parse_input(data):
    workflows = {}
    parts = []

    while data:
        line = data.pop(0)
        if line == "":
            break

        workflow_name = line.split("{")[0]
        workflow_rules = line.split("{")[1].split("}")[0].split(",")

        workflows[workflow_name] = workflow_rules

    while data:
        line = data.pop(0)
        matches = re.findall(r'([xmas])=(\d+)', line)
        parts.append({key: int(value) for key, value in matches})

    return workflows, parts


def is_accepted(part, result, workflows):
    if result == "A":
        return True
    elif result == "R":
        return False
    else:
        rules = workflows[result]
        for rule in rules:
            # Find the first rule that matches
            if ':' in rule:
                condition, next_result = rule.split(":")
                if eval(f"{part[condition[0]]}{condition[1:]}"):
                    return is_accepted(part, next_result, workflows)
            else:
                next_result = rule
                return is_accepted(part, next_result, workflows)


if __name__ == "__main__":
    with open("input.txt") as f:
        data = f.read().splitlines()

    workflows, parts = parse_input(data)

    print(workflows, parts)
    count = 0
    for part in parts:
        if is_accepted(part, "in", workflows):
            count += sum(part.values())
    print(count)
