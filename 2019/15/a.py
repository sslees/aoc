#! /usr/bin/env python3

import curses
import networkx as nx

NORTH, SOUTH, WEST, EAST, HALT = 1, 2, 3, 4, 5
START, WALL, PATH, FINISH = "S", "█", "╋", "F"
RED, GREEN, BLUE, YELLOW = 1, 2, 3, 4


def adjust(mode, address, memory, base):
    if mode == 0:  # position
        return memory[address]
    if mode == 1:  # immediate
        return address
    if mode == 2:  # relative
        return base + memory[address]
    raise Exception


def read_input(screen, graph, pos):
    # time.sleep(0.01)

    if pos in graph and graph.nodes[pos]["type"] == "finish":
        return next(iter(graph.in_edges(pos, data="dir")))[2]
    x, y = pos
    if (x, y - 1) not in graph:
        return NORTH
    if (x + 1, y) not in graph:
        return EAST
    if (x, y + 1) not in graph:
        return SOUTH
    if (x - 1, y) not in graph:
        return WEST
    if list(graph.predecessors(pos)):
        return next(iter(graph.in_edges(pos, data="dir")))[2]
    start = next(n for n in graph if graph.nodes[n]["type"] == "start")
    finish = next(n for n in graph if graph.nodes[n]["type"] == "finish")
    path = nx.shortest_path(graph, start, finish)
    path.remove(start)
    path.remove(finish)
    for n in path:
        screen.addch(n[1], n[0], PATH, curses.color_pair(GREEN) | curses.A_REVERSE)
    screen.refresh()
    graph_undir = graph.to_undirected()
    last = max(
        (n for n in graph_undir if graph_undir.nodes[n]["type"] == "path"),
        key=lambda n: nx.shortest_path_length(graph_undir, finish, n),
    )
    minutes = nx.shortest_path_length(graph_undir, finish, last)
    screen.addch(last[1], last[0], PATH, curses.color_pair(BLUE) | curses.A_REVERSE)
    screen.addstr(1, 1, "commands: {}, minutes: {}".format(len(path) + 1, minutes))
    screen.getch()
    return HALT


def write_output(screen, graph, pos, command, status):
    x, y = pos
    if command == NORTH:
        nxt = x, y - 1
        reverse = SOUTH
    elif command == SOUTH:
        nxt = x, y + 1
        reverse = NORTH
    elif command == WEST:
        nxt = x - 1, y
        reverse = EAST
    elif command == EAST:
        nxt = x + 1, y
        reverse = WEST
    else:
        raise Exception
    x2, y2 = nxt

    if status == 0:  # wall
        graph.add_node(nxt, type="wall")
        graph.add_edge(pos, nxt, dir=reverse)
        screen.addch(y2, x2, WALL, curses.color_pair(RED))
        screen.refresh()
        return pos
    if status == 1:  # moved
        if nxt not in graph:
            graph.add_node(nxt, type="path")
            graph.add_edge(pos, nxt, dir=reverse)
            screen.addch(y2, x2, PATH, curses.color_pair(BLUE))
            screen.refresh()
        return nxt
    if status == 2:  # done
        graph.add_node(nxt, type="finish")
        graph.add_edge(pos, nxt, dir=reverse)
        screen.addch(y2, x2, FINISH, curses.color_pair(YELLOW))
        screen.refresh()
        return nxt
    raise Exception


def main(stdscr):
    pointer, base = 0, 0
    with open("input.txt") as f:
        memory = list(map(int, f.readline().split(",")))
    memory.extend([0] * len(memory) * 10)
    pos = 22, 24
    graph = nx.DiGraph()
    graph.add_node(pos, type="start")
    curses.use_default_colors()
    curses.init_pair(RED, curses.COLOR_RED, -1)
    curses.init_pair(GREEN, curses.COLOR_GREEN, -1)
    curses.init_pair(BLUE, curses.COLOR_BLUE, -1)
    curses.init_pair(YELLOW, curses.COLOR_YELLOW, -1)
    stdscr.addch(pos[1], pos[0], START, curses.color_pair(YELLOW))
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
            command = read_input(stdscr, graph, pos)
            memory[address1] = command
            pointer += 2
        elif opcode == 4:  # output
            address1 = adjust(mode1, pointer + 1, memory, base)
            pos = write_output(stdscr, graph, pos, command, memory[address1])
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


if __name__ == "__main__":
    curses.wrapper(main)
