#! /bin/env python3

def main():
    with open("test.txt") as f:
        count = 0
        for line in f.readlines():
            line = line.rstrip()
            policy, passwd = line.split(": ")
            reps, letter = policy.split()
            low, high = reps.split("-")
            if bool(passwd[int(low) - 1] == letter) ^ bool(passwd[int(high) - 1] == letter):
                count += 1
    print(count)

if __name__ == "__main__":
    main()
