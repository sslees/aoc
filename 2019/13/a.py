#! /usr/bin/env python3

import curses
import time


def adjust(mode, address, memory, base):
    if mode == 0:  # position
        return memory[address]
    if mode == 1:  # immediate
        return address
    if mode == 2:  # relative
        return base + memory[address]
    raise Exception


def main(stdscr):
    pointer, base = 0, 0
    with open("input.txt") as f:
        memory = list(map(int, f.readline().split(",")))
    memory.extend([0] * len(memory) * 10)
    memory[0] = 2  # number of quarters inserted
    buff = []
    paddle, ball = None, None
    curses.curs_set(0)
    stdscr.clear()
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
            time.sleep(0.005)
            if paddle > ball:  # left
                ch = -1
            elif paddle < ball:  # right
                ch = 1
            else:  # neutral
                ch = 0
            memory[address1] = ch
            pointer += 2
        elif opcode == 4:  # output
            address1 = adjust(mode1, pointer + 1, memory, base)
            buff.append(memory[address1])
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
        if len(buff) == 3:
            ch, y, x = buff.pop(), buff.pop(), buff.pop()
            if x == -1 and y == 0:
                stdscr.addstr(0, 0, "score: {}".format(ch))
            else:
                if ch == 0:
                    ch = " "
                elif ch == 1:
                    ch = "#"
                elif ch == 2:
                    ch = "-"
                elif ch == 3:
                    ch = "="
                    paddle = x
                elif ch == 4:
                    ch = "."
                    ball = x
                stdscr.addch(y + 1, x, ch)
            stdscr.refresh()
    stdscr.getch()


curses.wrapper(main)
