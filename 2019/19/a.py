#! /usr/bin/env python3


def next_state(state):
    i, x, y, maxX, maxY, done = state
    if i == 2:
        x += 1
        if x > maxX:
            x = 0
            y += 1
        if x == maxX and y == maxY:
            done = True
    i = 1 if i == 2 else 2
    return i, x, y, maxX, maxY, done


def adjust(mode, address, memory, base):
    if mode == 0:  # position
        return memory[address]
    if mode == 1:  # immediate
        return address
    if mode == 2:  # relative
        return base + memory[address]
    raise Exception


def main():
    pointer, base = 0, 0
    with open("input.txt") as f:
        memory = list(map(int, f.readline().split(",")))
    save = memory.copy()
    memory.extend([0] * len(memory) * 10)
    state = 1, 0, 0, 49, 49, False
    count = 0
    while True:
        instr = "{:05}".format(memory[pointer])
        opcode = int(instr[-2:])
        mode3, mode2, mode1 = list(map(int, instr[:-2]))
        if opcode == 1:  # add
            address1 = adjust(mode1, pointer + 1, memory, base)
            address2 = adjust(mode2, pointer + 2, memory, base)
            address3 = adjust(mode3, pointer + 3, memory, base)
            memory[address3] = memory[address1] + memory[address2]
            pointer += 4
        elif opcode == 2:  # multiply
            address1 = adjust(mode1, pointer + 1, memory, base)
            address2 = adjust(mode2, pointer + 2, memory, base)
            address3 = adjust(mode3, pointer + 3, memory, base)
            memory[address3] = memory[address1] * memory[address2]
            pointer += 4
        elif opcode == 3:  # input
            address1 = adjust(mode1, pointer + 1, memory, base)
            memory[address1] = state[state[0]]
            pointer += 2
            state = next_state(state)
        elif opcode == 4:  # output
            address1 = adjust(mode1, pointer + 1, memory, base)
            if memory[address1]:
                count += 1
            pointer += 2
        elif opcode == 5:  # jump true
            address1 = adjust(mode1, pointer + 1, memory, base)
            address2 = adjust(mode2, pointer + 2, memory, base)
            pointer = memory[address2] if memory[address1] else pointer + 3
        elif opcode == 6:  # jump false
            address1 = adjust(mode1, pointer + 1, memory, base)
            address2 = adjust(mode2, pointer + 2, memory, base)
            pointer = pointer + 3 if memory[address1] else memory[address2]
        elif opcode == 7:  # less than
            address1 = adjust(mode1, pointer + 1, memory, base)
            address2 = adjust(mode2, pointer + 2, memory, base)
            address3 = adjust(mode3, pointer + 3, memory, base)
            memory[address3] = 1 if memory[address1] < memory[address2] else 0
            pointer += 4
        elif opcode == 8:  # equal to
            address1 = adjust(mode1, pointer + 1, memory, base)
            address2 = adjust(mode2, pointer + 2, memory, base)
            address3 = adjust(mode3, pointer + 3, memory, base)
            memory[address3] = 1 if memory[address1] == memory[address2] else 0
            pointer += 4
        elif opcode == 9:  # adjust base
            address1 = adjust(mode1, pointer + 1, memory, base)
            base += memory[address1]
            pointer += 2
        elif opcode == 99:  # halt
            if state[-1]:  # done
                print(count)
                break
            pointer, base = 0, 0
            memory = save.copy()
            memory.extend([0] * len(memory) * 10)
        else:
            raise Exception


if __name__ == "__main__":
    main()
