# Answer: 788081152

from math import prod


def get_circuit(input):
    circuit = {}
    for line in input:
        id, output = line.split(' -> ')
        module_type = id[0] if id[0] in ['&', '%'] else id
        id = id[1:] if id[0] in ['&', '%'] else id
        circuit[id] = {
            'type': module_type,
            'input': [],
            'output': output.split(', ')
        }
    # Find inputs for each node
    for module in circuit:
        for output in circuit[module]['output']:
            if output in circuit:
                circuit[output]['input'].append(module)

    return circuit


def get_state(circuit):
    state = {}
    for module in circuit:
        if circuit[module]['type'] == '%':
            state[module] = False
        elif circuit[module]['type'] == '&':
            state[module] = {m: False for m in circuit[module]['input']}
    return state


if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        input = f.read().splitlines()

    circuit = get_circuit(input)
    state = get_state(circuit)

    # print(circuit)
    # print(state)

    pulse_count = {
        # False = low, True = high
        False: 0,
        True: 0
    }

    for p in range(0, 1000):

        print(f"------ button press {p+1} -------")
        queue = [('button', 'broadcaster', False)]

        while queue:
            prev_mod, mod, pulse_in = queue.pop(0)
            print(f"{prev_mod} -{'high' if pulse_in else 'low'} -> {mod}")

            pulse_count[pulse_in] += 1

            if mod in circuit:
                # Calculate the state of the current module
                module_type = circuit[mod]['type']
                if module_type == '%':
                    if pulse_in == False:
                        # Invert the current state of the module
                        state[mod] = not state[mod]
                        pulse_out = state[mod]
                    else:
                        continue
                elif module_type == '&':
                    state[mod][prev_mod] = pulse_in
                    # Check if all inputs are high
                    if all(state[mod].values()):
                        pulse_out = False
                    else:
                        pulse_out = True
                else:
                    pulse_out = pulse_in
                # Add the next modules to the queue
                queue.extend([(mod, output_mod, pulse_out) for output_mod in circuit[mod]['output']])

    print(prod(pulse_count.values()))
