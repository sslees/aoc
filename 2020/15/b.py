#! /bin/env python3


def main():
    with open("input.txt") as f:
        d = [int(l.strip()) for l in f.readline().split(",")]
    more = {}
    when = {}
    for i, e in enumerate(d):
        if e in when:
            more[e] = when[e]
        when[e] = i + 1
    last = d[-1]
    for i in range(len(d) + 1, 30000001):
        if last not in more:
            say = 0
        else:
            say = when[last] - more[last]
        if say in when:
            more[say] = when[say]
        when[say] = i
        last = say
    print(say)


if __name__ == "__main__":
    main()
