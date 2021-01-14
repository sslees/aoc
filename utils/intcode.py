from collections import defaultdict


class Computer:
    def __init__(self, program, read, write):
        self.mem = defaultdict(int, enumerate(program))
        self.read = read
        self.write = write
        self.ptr = 0
        self.base = 0

    def param(self, mode):
        self.ptr += 1
        if mode == 0:  # position
            return self.mem[self.ptr]
        if mode == 1:  # immediate
            return self.ptr
        if mode == 2:  # relative
            return self.base + self.mem[self.ptr]
        raise Exception

    def step(self):
        instr = "{:05}".format(self.mem[self.ptr])
        op = int(instr[-2:])
        modes = list(map(int, instr[-3::-1]))
        if op == 1:  # add
            a1, a2, a3 = map(self.param, modes[:3])
            self.mem[a3] = self.mem[a1] + self.mem[a2]
        elif op == 2:  # multiply
            a1, a2, a3 = map(self.param, modes[:3])
            self.mem[a3] = self.mem[a1] * self.mem[a2]
        elif op == 3:  # input
            a1 = self.param(modes[0])
            self.mem[a1] = self.read()
        elif op == 4:  # output
            a1 = self.param(modes[0])
            self.write(self.mem[a1])
        elif op == 5:  # jump true
            a1, a2 = map(self.param, modes[:2])
            self.ptr = self.mem[a2] - 1 if self.mem[a1] else self.ptr
        elif op == 6:  # jump false
            a1, a2 = map(self.param, modes[:2])
            self.ptr = self.ptr if self.mem[a1] else self.mem[a2] - 1
        elif op == 7:  # less than
            a1, a2, a3 = map(self.param, modes[:3])
            self.mem[a3] = 1 if self.mem[a1] < self.mem[a2] else 0
        elif op == 8:  # equal to
            a1, a2, a3 = map(self.param, modes[:3])
            self.mem[a3] = 1 if self.mem[a1] == self.mem[a2] else 0
        elif op == 9:  # adjust base
            a1 = self.param(modes[0])
            self.base += self.mem[a1]
        elif op == 99:  # halt
            return False
        else:
            raise Exception
        self.ptr += 1
        return True
