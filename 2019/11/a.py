#! /usr/bin/env python3


def adjust(mode, address, memory, base):
    if mode == 0:  # position
        return memory[address]
    if mode == 1:  # immediate
        return address
    if mode == 2:  # relative
        return base + memory[address]
    raise Exception


def look(grid, x, y):
    return grid[x, y] if (x, y) in grid else 0


def paint(grid, x, y, val):
    grid[x, y] = val
    print(x, y)


def move(x, y, direction, val):
    if val == 0:
        direction -= 90
    else:
        direction += 90
    direction = (direction + 360) % 360
    if direction == 0:
        return x, y + 1, direction
    if direction == 90:
        return x + 1, y, direction
    if direction == 180:
        return x, y - 1, direction
    if direction == 270:
        return x - 1, y, direction
    raise Exception


def main():
    pointer, base = 0, 0
    with open('input.txt') as f:
        memory = list(map(int, f.readline().split(',')))
    memory.extend([0] * len(memory) * 10)
    grid, x, y, direction, painted = {}, 0, 0, 0, False
    while True:
        instr = '{:05}'.format(memory[pointer])
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
            memory[address1] = int(look(grid, x, y))
            pointer += 2
        elif opcode == 4:  # output
            address1 = adjust(mode1, pointer + 1, memory, base)
            if not painted:
                paint(grid, x, y, memory[address1])
            else:
                x, y, direction = move(x, y, direction, memory[address1])
            painted = not painted
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
            break
        else:
            raise Exception


if __name__ == '__main__':
    main()
