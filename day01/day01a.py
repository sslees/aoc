import itertools

def main():
    with open("input.txt") as f:
        for a, b in itertools.combinations(f.readlines(), 2):
            a = int(a)
            b = int(b)
            if a + b == 2020:
                print(a * b)

if __name__ == "__main__":
    main()
